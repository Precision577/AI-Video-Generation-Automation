import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import os

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")  # Debug print
    else:
        print(f"Directory already exists: {path}")  # Debug print

def process_script():
    input_text = script_text_box.get("1.0", tk.END)
    lines = input_text.strip().split('\n')
    
    spoken_script = []
    color_script = []
    image_prompts = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('"'):
            spoken_script.append(line.strip('"'))
        elif line.lower().startswith('colors:'):
            color_script.append(line)
        elif line.lower().startswith('image prompt:'):
            image_prompt = line[13:].strip('" ').strip()  # Removes the "Image prompt: " part and any trailing quotes or spaces
            image_prompts.append(image_prompt + "\n")
    
    # Ensure directories exist
    ensure_directory('spoken_script')
    ensure_directory('colors')
    ensure_directory('image_prompts')

    # Save the outputs
    with open('spoken_script/spoken_script.txt', 'w') as file:
        file.write('\n\n'.join(spoken_script))
    with open('colors/colors.txt', 'w') as file:
        file.write('\n'.join(color_script))
    with open('image_prompts/image_prompts.txt', 'w') as file:
        file.write('\n'.join(image_prompts))
    
    messagebox.showinfo("Success", "Files saved: spoken_script.txt, colors.txt, image_prompts.txt")
    script_text_box.delete('1.0', tk.END)

def select_all(event=None):
    script_text_box.tag_add(tk.SEL, "1.0", tk.END)
    script_text_box.mark_set(tk.INSERT, "1.0")
    script_text_box.see(tk.INSERT)
    return 'break'

# Set up the GUI
root = tk.Tk()
root.title("Script Processor")

# Create a scrolled text box for input
script_text_box = scrolledtext.ScrolledText(root, width=60, height=20)
script_text_box.pack(pady=10)

# Bind select all to Ctrl+A
root.bind_class("Text", "<Control-a>", select_all)
root.bind_class("Text", "<Control-A>", select_all)  # Just in case caps lock is on

# Create a process button
process_button = tk.Button(root, text="Process Script", command=process_script)
process_button.pack(pady=5)

# Run the GUI
root.mainloop()

