import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Predefined scripts
PREDEFINED_SCRIPTS = [
    "D:/dev/cuesplit/split.py",  # Replace with the actual path to your script
    "D:/dev/toFormat/toFormatMovesWrapped.py",  # Replace with the actual path to your script
]

def run_script():
    selected_script = script_selector.get(tk.ACTIVE)
    if not selected_script:
        messagebox.showerror("Error", "Please select a script to run.")
        return
    
    user_input = input_field.get()
    try:
        # Run the selected script with subprocess
        command = f"{selected_script} {user_input}"
        process = subprocess.run(command, shell=True, text=True, capture_output=True)
        
        # Display output
        output_text.delete(1.0, tk.END)
        if process.stdout:
            output_text.insert(tk.END, "Output:\n" + process.stdout)
        if process.stderr:
            output_text.insert(tk.END, "\nError:\n" + process.stderr)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run the script: {e}")

def browse_scripts():
    file_path = filedialog.askopenfilename(
        title="Select a Script",
        filetypes=(("Python Scripts", "*.py"), ("Batch Files", "*.bat"), ("All Files", "*.*")),
    )
    if file_path:
        script_selector.insert(tk.END, file_path)

# Create the GUI
root = tk.Tk()
root.title("Script Runner")

# Script Selector
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Available Scripts:").grid(row=0, column=0, padx=5, pady=5)
script_selector = tk.Listbox(frame, width=50, height=10)
script_selector.grid(row=1, column=0, padx=5, pady=5)
browse_button = tk.Button(frame, text="Browse...", command=browse_scripts)
browse_button.grid(row=1, column=1, padx=5, pady=5)

# Add predefined scripts to the list
for script in PREDEFINED_SCRIPTS:
    script_selector.insert(tk.END, script)

# Input Field
tk.Label(root, text="Enter Parameters:").pack(pady=5)
input_field = tk.Entry(root, width=50)
input_field.pack(pady=5)

# Run Button
run_button = tk.Button(root, text="Run Script", command=run_script)
run_button.pack(pady=10)

# Output Display
tk.Label(root, text="Script Output:").pack(pady=5)
output_text = tk.Text(root, height=15, width=70)
output_text.pack(pady=5)

# Start the GUI loop
root.mainloop()


