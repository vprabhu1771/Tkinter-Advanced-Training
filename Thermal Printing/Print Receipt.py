import tkinter as tk
from escpos.printer import Usb

# Configure your printer (adjust vendor_id and product_id for your printer)
try:
    printer = Usb(0x0416, 0x5011)
except Exception as e:
    print("Printer not found:", e)

# Function to add a product to the receipt
def add_product():
    name = product_name.get()
    qty = int(product_qty.get())
    price = float(product_price.get())
    subtotal = qty * price
    grand_total[0] += subtotal

    # Display the product details in the listbox
    receipt_list.insert(tk.END, f"{name:20} {qty:5} {price:8.2f} {subtotal:10.2f}")

    # Clear input fields
    product_name.delete(0, tk.END)
    product_qty.delete(0, tk.END)
    product_price.delete(0, tk.END)

# Function to print the receipt
def print_receipt():
    try:
        printer.text("====== Receipt ======\n")
        printer.text(f"{'Product':20} {'Qty':5} {'Price':8} {'SubTotal':10}\n")
        printer.text("=" * 40 + "\n")

        for line in receipt_list.get(0, tk.END):
            printer.text(line + "\n")

        printer.text("=" * 40 + "\n")
        printer.text(f"{'Grand Total':30} {grand_total[0]:.2f}\n")
        printer.text("=" * 40 + "\n")
        printer.cut()
    except Exception as e:
        print("Error printing receipt:", e)

# Initialize tkinter GUI
root = tk.Tk()
root.title("Receipt Printer")

# Variables
grand_total = [0.0]  # Grand total stored in a list for mutability

# Entry fields for product details
tk.Label(root, text="Product Name:").pack()
product_name = tk.Entry(root, width=30)
product_name.pack()

tk.Label(root, text="Quantity:").pack()
product_qty = tk.Entry(root, width=30)
product_qty.pack()

tk.Label(root, text="Price:").pack()
product_price = tk.Entry(root, width=30)
product_price.pack()

# Add Product Button
add_button = tk.Button(root, text="Add Product", command=add_product)
add_button.pack(pady=10)

# Listbox for receipt preview
receipt_list = tk.Listbox(root, width=60)
receipt_list.pack(pady=10)

# Print Receipt Button
print_button = tk.Button(root, text="Print Receipt", command=print_receipt)
print_button.pack(pady=10)

root.mainloop()