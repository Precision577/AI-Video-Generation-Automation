# AI Video Generation Automation

## Project Overview
This repository automates the creation of AI-generated videos using GPT-generated scripts, DALL-E-generated images, and Eleven Labs voiceovers. The workflow seamlessly integrates text generation, color-coded visual effects, and image-based storytelling to produce high-quality, visually engaging videos.

---

## Features

### 1. Dynamic Script and Media Generation
- **Custom GPT Script Generator**: Generate scripts, color codes, and image prompts based on product or topic input.
- **Image Generation**: Create high-quality images with DALL-E based on generated prompts.
- **AI Voiceovers**: Use Eleven Labs to convert text scripts into high-quality audio.

### 2. Streamlined Workflow
- **Extract Script Details**: Break down the GPT output into structured files for spoken script, colors, and image prompts.
- **Remove Pauses**: Automatically remove awkward pauses from audio for smoother playback.
- **Timestamp Alignment**: Generate precise word timings for subtitle placement using Aeneas.

### 3. Automated Video Creation
- **Image and Subtitle Integration**: Overlay subtitles on generated images with color-coded highlights.
- **Audio Synchronization**: Sync audio to video with exact timing for a polished output.
- **Final Video Rendering**: Combine audio, images, and subtitles to create a professional video.

### 4. Efficient Resource Management
- **Parallel Processing**: Use multiprocessing to speed up video segment generation.
- **Temporary File Cleanup**: Automatically delete intermediate files to save space.

---

## Use Cases
This project is ideal for:
- **Product Marketing**: Generate compelling videos for products or services.
- **Storytelling**: Create AI-driven narratives with dynamic visuals and audio.
- **Content Automation**: Automate video production for social media or educational content.

---

## Workflow and Architecture

### 1. Script and Media Preparation
#### Script Generation:
- Use the **Custom GPT Script Generator** to generate text scripts, colors, and image prompts.
  - **Example Input**: Portable Charger
  - **Example Output**:
    - Spoken script lines.
    - Color-coded word emphasis.
    - Image prompts for DALL-E.

#### Extract Script Details:
- Use `extract.py` to generate:
  - **Spoken Script**: Text for audio generation.
  - **Color Script**: Color codes for visual emphasis.
  - **Image Prompts**: Prompts for DALL-E.

#### Image Generation:
- Generate images from prompts using DALL-E or its API.
- Save images in the `photos` directory, ensuring filenames match the line numbers (e.g., `1.png`).

#### Audio Generation:
- Upload the spoken script to **Eleven Labs**.
- Save the output audio to the `audio` directory.
- Use `removepauses.py` to refine the audio.

### 2. Video Creation
#### Timestamp Alignment:
- Run `bash run_aeneas.sh` to align audio with text and generate timestamps in JSON format.

#### Generate Video Segments:
- Use `create_video.py` to:
  - Overlay subtitles on images with color-coded highlights.
  - Synchronize images and subtitles with audio timestamps.
  - Generate video segments for each script line.

#### Concatenate and Finalize:
- Merge video segments into a single video.
- Add synchronized audio for the final output.
  - **Output**: The final video is saved in the `output` directory.

---

## Technologies Used

### Programming Languages
- **Python 3.11**: Core logic for processing scripts, images, and videos.
- **Bash**: Automates audio alignment with Aeneas.

### Libraries and Frameworks
- **MoviePy**: Video processing and creation.
- **Pillow**: Image editing and subtitle overlay.
- **Aeneas**: Timestamp alignment for subtitles and audio.
- **DALL-E API**: Image generation from prompts.
- **Tkinter**: GUI for script extraction.

---

## System Design
1. **Script Processing**:
   - Extracts and organizes GPT-generated content.
2. **Image and Audio Integration**:
   - Combines visuals and audio dynamically.
3. **Video Rendering**:
   - Generates subtitle overlays and synchronizes them with the visuals and audio.

---

## Setup Instructions

### 1. Install Prerequisites
#### Python 3.11 and Pip:
```bash
sudo apt-get install python3.11 python3-pip -y


```
### Install Required Libraries
bash
pip install -r requirements.txt

### Generate Scripts
Use the Custom GPT script generator to create content.

### Run the Workflow

Step 1: Extract Scripts
bash
python3 extract.py

Step 2: Generate Images
Paste prompts into DALL-E or its API.
Save images in the photos directory with matching filenames.

Step 3: Generate Audio
Use Eleven Labs to create audio files.
Save in the audio directory and run removepauses.py:
bash
python3 removepauses.py

Step 4: Align Audio with Script
bash
bash run_aeneas.sh

Step 5: Create Video
bash
python3 create_video.py

### Example Workflow
Input: Portable Charger.
Generate GPT output: Script, colors, and image prompts.
Process script: Use extract.py.
Generate images: Use DALL-E.
Generate audio: Use Eleven Labs.
Run: run_aeneas.sh for timestamps.
Create video: Use create_video.py.

### Key Features in Code

Script Processing
Extract spoken scripts, color coding, and image prompts.

Video Creation
Subtitle overlay with dynamic color coding.
High-quality image zoom and cropping for 9:16 aspect ratio.
Multiprocessing for fast video segment generation.

Error Handling
Verifies file existence at each step.
Ensures synchronization of audio and visuals.

### Conclusion
This project demonstrates expertise in:

AI Media Integration:
Using GPT, DALL-E, and Eleven Labs for seamless content generation.

Example Video:


Video Production:
Automating the entire video creation process with Python.

Scalable Workflows:
Efficiently managing resources with multiprocessing and dynamic file handling.

Example Video:

[Click here to watch the video](example%20videos%20and%20scripts/final_video_with_audio.mp4)

