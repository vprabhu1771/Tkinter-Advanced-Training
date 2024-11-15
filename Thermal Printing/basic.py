import tkinter as tk
from escpos.printer import Usb

# Setup your ESC/POS printer connection here
# Adjust the vendor and product ID to match your USB printer
# Example: (vendor=0x04b8, product=0x0e15) for some Epson printers
try:
    printer = Usb(0x0416, 0x5011)
except Exception as e:
    print("Printer not found:", e)

# Function to print text from entry box
def print_text():
    text = text_entry.get()
    try:
        printer.text(text + "\n")
        printer.cut()
    except Exception as e:
        print("Error printing:", e)

# Set up tkinter GUI
root = tk.Tk()
root.title("ESC/POS Printer")

# Create entry box for text
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

# Print button
print_button = tk.Button(root, text="Print", command=print_text)
print_button.pack(pady=5)

root.mainloop()