#!/bin/bash

# Set the base directory to the location of this script
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

# Find the .txt file in the spoken_script directory
TXT_FILE=$(find "$BASE_DIR/spoken_script" -name "*.txt" | head -n 1)

# Find the .mp3 file in the audio directory
MP3_FILE=$(find "$BASE_DIR/audio" -name "*.mp3" | head -n 1)

# Define the output directory and file
OUTPUT_DIR="$BASE_DIR/aligned_script_with_timestamps"
OUTPUT_FILE="$OUTPUT_DIR/aligned_output.json"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Check if both files were found
if [[ -z "$TXT_FILE" ]] || [[ -z "$MP3_FILE" ]]; then
    echo "Error: Text file or audio file not found."
    exit 1
fi

# Run Aeneas
aeneas_execute_task "$MP3_FILE" "$TXT_FILE" "task_language=eng|is_text_type=plain|os_task_file_format=json" "$OUTPUT_FILE"

# Check if Aeneas was successful
if [ $? -eq 0 ]; then
    echo "Alignment completed successfully. Output saved to $OUTPUT_FILE"
else
    echo "Aeneas failed to process the files."
fi
