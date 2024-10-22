To run actual system commands like `ls`, `mkdir`, `cp`, and `rmdir`, you can use Python's `subprocess` module to execute these commands and capture their success or failure. Here’s how you can modify the previous code to run these system commands and display the result in the `tkinter` text area:

### Full Example:

```python
import tkinter as tk
from tkinter import ttk
import subprocess

# Function to execute commands and display the result
def execute_command(commands):
    status_text.config(state='normal')  # Enable text widget
    for command in commands:
        # Display the command being run
        status_text.insert(tk.END, f"Running: {command}...\n")
        root.update()

        # Execute the command using subprocess
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Check if the command was successful (returncode 0 means success)
            if result.returncode == 0:
                status_text.insert(tk.END, f"{command} [OK]\n")
            else:
                status_text.insert(tk.END, f"{command} [Error]: {result.stderr}\n")
        except Exception as e:
            status_text.insert(tk.END, f"{command} [Error]: {str(e)}\n")
        
        root.update()
        root.after(1000)  # Simulate delay for 1 second
    
    status_text.config(state='disabled')  # Disable text widget after updating

# Create the tkinter window
root = tk.Tk()
root.title("Command Execution")

# Create a disabled text widget for displaying status
status_text = tk.Text(root, height=12, width=50, font=("Arial", 12))
status_text.pack(pady=20)
status_text.config(state='disabled')  # Initially disabled

# Command array to be passed for execution
commands_to_run = ["mkdir abcd", "dir"]

# Create and position the execute button, passing the commands array
execute_button = ttk.Button(root, text="Execute", command=lambda: execute_command(commands_to_run))
execute_button.pack(pady=10)

# Run the tkinter main loop
root.mainloop()
```

### Explanation:
1. **`subprocess.run`**: Executes each command in the `commands_to_run` list. The `shell=True` option allows commands to be passed as strings (like you would type in a terminal). It captures both `stdout` (standard output) and `stderr` (standard error).
2. **`result.returncode`**: If the command is successful (returns 0), it displays `[OK]`. If the command fails, it shows `[Error]` along with the error message from `stderr`.
3. **Error Handling**: In case of an exception (e.g., invalid command), it catches the exception and displays an `[Error]` message with the error details.

### How it Works:
- It will execute commands like `ls` (list files), `mkdir abcd` (create a directory), `cp file.txt copy.txt` (copy a file), and `rmdir abcd` (remove a directory).
- The result of each command will be displayed in the text area, showing `[OK]` for success or `[Error]` with a message if something goes wrong.

### Notes:
- Ensure you have a file named `file.txt` in the working directory if you're using the `cp` command in the example.
- The `mkdir abcd` and `rmdir abcd` commands will create and remove the directory `abcd` as expected.