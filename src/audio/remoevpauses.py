
from pydub import AudioSegment, silence
import os

def remove_long_pauses_from_directory(directory, output_suffix="_no_long_pauses_more_aggressive"):
    """
    Scans a directory for MP3 files, processes each to remove long pauses with aggressive settings,
    and saves the processed files in the same directory with a specific suffix added to their names.

    Parameters:
    - directory: The directory to scan for MP3 files and save the processed files.
    - output_suffix: Suffix to add to the original filenames for the processed files.
    """
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            file_path = os.path.join(directory, filename)
            print(f"Processing: {file_path}")

            # Load the audio file
            audio = AudioSegment.from_mp3(file_path)

            # Parameters for very aggressive silence removal
            min_silence_len = 250  # Consider very short pauses as silence, in milliseconds
            silence_thresh = -52  # More sensitive to quieter sounds, in dB
            keep_silence = 100  # Keep 200 milliseconds of silence at the start and end of each chunk

            # Split audio where silence is detected and get chunks
            chunks = silence.split_on_silence(audio, 
                                              min_silence_len=min_silence_len,
                                              silence_thresh=silence_thresh, 
                                              keep_silence=keep_silence)

            # Create a new, processed audio segment
            processed_audio = AudioSegment.empty()
            for chunk in chunks:
                processed_audio += chunk

            # Define output file path
            base_filename, file_extension = os.path.splitext(file_path)
            output_file_path = f"{base_filename}{output_suffix}{file_extension}"

            # Export the processed audio to a new file
            processed_audio.export(output_file_path, format="mp3")
            print(f"Processed file saved to: {output_file_path}")

if __name__ == "__main__":
    # Use the current directory where the script is running
    current_directory = os.getcwd()
    
    # Process all MP3 files in the current directory
    remove_long_pauses_from_directory(current_directory)
