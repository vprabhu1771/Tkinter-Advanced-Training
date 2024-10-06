# Tkinter MD5 Password Checker

# https://www.md5hashgenerator.com/

To create a Tkinter GUI for MD5 hash comparison, where you can input a hash value and select a password guess file, here's a step-by-step guide:

1. A text field to input the MD5 hash.
2. A file picker to load the password guess file (containing a list of passwords).
3. Compare each password in the file with the MD5 hash.
4. Display the matched password if found.

Here is a Python example using Tkinter:

```python
import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib

# Function to compute the MD5 hash of a string
def compute_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

# Function to pick a file
def pick_file():
    file_path = filedialog.askopenfilename(title="Select Password Guess File")
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Function to run the MD5 hash comparison
def run_md5_comparison():
    md5_hash = hash_entry.get()
    file_path = file_entry.get()

    if not md5_hash or not file_path:
        messagebox.showerror("Error", "Please provide both MD5 hash and password file.")
        return

    try:
        with open(file_path, 'r') as file:
            for line in file:
                password = line.strip()
                if compute_md5(password) == md5_hash:
                    result_label.config(text=f"Password found: {password}")
                    return

        result_label.config(text="Password not found in the file.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")

# Set up the GUI window
root = tk.Tk()
root.title("MD5 Hash Password Finder")

# Hash input field
tk.Label(root, text="Enter MD5 Hash:").pack(pady=5)
hash_entry = tk.Entry(root, width=50)
hash_entry.pack(pady=5)

# File picker for password guess file
tk.Label(root, text="Password Guess File:").pack(pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)
file_button = tk.Button(root, text="Browse", command=pick_file)
file_button.pack(pady=5)

# Button to run the comparison
run_button = tk.Button(root, text="Run", command=run_md5_comparison)
run_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
```

### How it works:
1. You input the MD5 hash into the text field.
2. Use the file picker to select a file that contains the list of password guesses.
3. The program computes the MD5 hash of each password in the file and compares it with the entered MD5 hash.
4. If a match is found, it displays the corresponding password.

Let me know if you need further adjustments!