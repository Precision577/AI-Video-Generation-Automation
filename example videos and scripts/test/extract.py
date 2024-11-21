import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def process_script():
    input_text = script_text_box.get("1.0", tk.END)
    lines = input_text.strip().split('\n')
    
    # Initialize lists to hold different parts of the script
    spoken_script = []
    color_script = []
    image_prompts = []
    
    for i, line in enumerate(lines):
        # Handle spoken script
        if line.startswith('"'):
            spoken_script.append(line.strip('"'))
        # Handle colors
        elif line.startswith('Colors:'):
            color_script.append(line)
        # Handle image prompts with added spacing for readability
        elif line.startswith('Image prompt:'):
            image_prompt = line.replace('Image prompt: "', '').rstrip('"')
            image_prompts.append(image_prompt + "\n")
    
    # Add concluding line to spoken script if present
    if "Concluding line:" in input_text:
        conclusion_start = input_text.index("Concluding line:") + len("Concluding line:")
        concluding_line = input_text[conclusion_start:].strip()
        spoken_script.append(concluding_line)

    # Save the outputs to files
    with open('spoken_script.txt', 'w') as file:
        file.write('\n\n'.join(spoken_script))
    with open('color_script.txt', 'w') as file:
        file.write('\n'.join(color_script))
    with open('image_prompts.txt', 'w') as file:
        file.write('\n'.join(image_prompts))
    
    messagebox.showinfo("Success", "Files saved: spoken_script.txt, color_script.txt, image_prompts.txt")
    script_text_box.delete('1.0', tk.END)  # Clear the text box for new input

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

