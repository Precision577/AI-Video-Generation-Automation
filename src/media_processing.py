from moviepy.editor import CompositeVideoClip, ImageClip, AudioFileClip
import os
import subprocess
import logging
from PIL import Image, ImageDraw, ImageFont
from utility import find_files_with_extension, load_json_file
from config import *

def create_dynamic_subtitle_clip(word, color_coding, font_size, output_width, output_height, start_time, duration, output_directory):
    logging.debug("Creating subtitle image for word: " + word)
    image_path = os.path.join(output_directory, f"{word}.png")
    image = create_subtitle_image(word, color_coding, font_size, output_width, output_height)
    image.save(image_path)
    
    clip = ImageClip(image_path).set_duration(duration).set_start(start_time)
    return clip, image_path

def generate_video_with_transitions(word_data, transitions, photo_files, audio_path, output_directory):
    logging.info("Generating video with transitions based on word data.")
    final_clips = []
    all_image_paths = []
    current_photo_index = 0

    for index, fragment in enumerate(word_data['fragments']):
        words = fragment['lines'][0].split()
        start_time = float(fragment['begin'])
        next_start_time = float(fragment['end'])
        duration = next_start_time - start_time

        # Check if we need to switch the photo
        if words[-1] in transitions:
            photo_path = photo_files[current_photo_index % len(photo_files)]
            current_photo_index += 1
        
        clips = []
        for word in words:
            clip, image_path = create_dynamic_subtitle_clip(word, color_coding, FONT_SIZE, OUTPUT_WIDTH, 200, start_time, duration, output_directory)
            clips.append(clip)
            all_image_paths.append(image_path)
        
        photo_clip = ImageClip(photo_path).set_duration(duration).set_start(start_time).resize(height=OUTPUT_HEIGHT)
        video_clip = CompositeVideoClip([photo_clip] + clips).set_position("center")
        audio_clip = AudioFileClip(audio_path).subclip(start_time, next_start_time)
        video_clip = video_clip.set_audio(audio_clip)

        segment_path = os.path.join(output_directory, f"segment_{index}.mp4")
        video_clip.write_videofile(segment_path, fps=30, codec='libx264', audio_codec='aac')
        final_clips.append(segment_path)
        logging.debug(f"Segment {index} saved to {segment_path}")

    return final_clips, all_image_paths

def concatenate_segments(segment_paths, output_path):
    logging.info("Concatenating segments into final video.")
    filelist_path = os.path.join(OUTPUT_DIR, 'filelist.txt')
    with open(filelist_path, 'w') as filelist:
        for path in segment_paths:
            filelist.write(f"file '{path}'\n")

    ffmpeg_command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', filelist_path,
        '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', output_path
    ]
    subprocess.run(ffmpeg_command, check=True)
    logging.info("Final video created at: " + output_path)

