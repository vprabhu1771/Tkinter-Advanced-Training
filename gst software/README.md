```
https://www.youtube.com/watch?v=bQPUXJJ1eDs
```

Here's a complete example of a GST Filing software using Tkinter, SQLite for database storage, and organized with folder setup.

### Folder Structure

```
gst_filing/
│
├── app.py                # Main application code (Tkinter UI)
├── database.py           # SQLite database setup and operations
├── gst_calculator.py     # GST calculation functions
├── models.py             # Models for database interaction
├── utils.py              # Utility functions like validation
├── requirements.txt      # Dependencies (if needed)
└── gst_filing.db         # SQLite database file
```

### 1. `requirements.txt`
You may need the following packages:
```txt
tkinter
sqlite3
```

Install dependencies if necessary:
```bash
pip install -r requirements.txt
```

### 2. `database.py`
This file handles database connections and setup.

```python
import sqlite3

def init_db():
    # Create a database or connect to an existing one
    conn = sqlite3.connect("gst_filing.db")
    cursor = conn.cursor()

    # Create the invoices table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS invoices (
                        id INTEGER PRIMARY KEY,
                        customer_name TEXT,
                        total_amount REAL,
                        gst_amount REAL,
                        invoice_number TEXT,
                        cgst REAL,
                        sgst REAL
                    )''')
    conn.commit()
    conn.close()

def save_invoice(customer_name, total_amount, gst_amount, invoice_number, cgst, sgst):
    conn = sqlite3.connect("gst_filing.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO invoices (customer_name, total_amount, gst_amount, invoice_number, cgst, sgst) VALUES (?, ?, ?, ?, ?, ?)", 
                   (customer_name, total_amount, gst_amount, invoice_number, cgst, sgst))
    conn.commit()
    conn.close()

def get_all_invoices():
    conn = sqlite3.connect("gst_filing.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invoices")
    invoices = cursor.fetchall()
    conn.close()
    return invoices
```

### 3. `gst_calculator.py`
Contains the GST calculation logic.

```python
def calculate_gst(total_amount):
    cgst = total_amount * 0.09
    sgst = total_amount * 0.09
    gst_amount = cgst + sgst
    return cgst, sgst, gst_amount
```

### 4. `models.py`
Optional, to manage structured models for the application. This could be expanded to include additional functionality if needed, but for now it acts as a representation of data.

```python
class Invoice:
    def __init__(self, customer_name, total_amount, gst_amount, invoice_number, cgst, sgst):
        self.customer_name = customer_name
        self.total_amount = total_amount
        self.gst_amount = gst_amount
        self.invoice_number = invoice_number
        self.cgst = cgst
        self.sgst = sgst
```

### 5. `utils.py`
Contains utility functions like validation.

```python
from tkinter import messagebox

def validate_input(customer_name, total_amount, invoice_number):
    if not customer_name:
        messagebox.showerror("Input Error", "Customer name is required.")
        return False
    if not total_amount or total_amount <= 0:
        messagebox.showerror("Input Error", "Total amount must be greater than zero.")
        return False
    if not invoice_number:
        messagebox.showerror("Input Error", "Invoice number is required.")
        return False
    return True
```

### 6. `app.py` - Type 1
This is the main Tkinter application file.

```python
import tkinter as tk
from tkinter import messagebox
from database import init_db, save_invoice, get_all_invoices
from gst_calculator import calculate_gst
from utils import validate_input

# Initialize the database
init_db()

# Setup Tkinter window
root = tk.Tk()
root.title("GST Filing Software")

# Create the Tkinter widgets
tk.Label(root, text="Customer Name:").grid(row=0, column=0)
customer_name_entry = tk.Entry(root)
customer_name_entry.grid(row=0, column=1)

tk.Label(root, text="Total Amount:").grid(row=1, column=0)
total_amount_entry = tk.Entry(root)
total_amount_entry.grid(row=1, column=1)

tk.Label(root, text="Invoice Number:").grid(row=2, column=0)
invoice_number_entry = tk.Entry(root)
invoice_number_entry.grid(row=2, column=1)


def save_invoice_button():
    customer_name = customer_name_entry.get()
    try:
        total_amount = float(total_amount_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
        return
    invoice_number = invoice_number_entry.get()

    if not validate_input(customer_name, total_amount, invoice_number):
        return

    cgst, sgst, gst_amount = calculate_gst(total_amount)

    save_invoice(customer_name, total_amount, gst_amount, invoice_number, cgst, sgst)

    # Clear the input fields after saving
    customer_name_entry.delete(0, tk.END)
    total_amount_entry.delete(0, tk.END)
    invoice_number_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Invoice saved successfully.")


# Button to save invoice
save_button = tk.Button(root, text="Save Invoice", command=save_invoice_button)
save_button.grid(row=3, column=0, columnspan=2)


def view_invoices():
    invoices = get_all_invoices()
    if not invoices:
        messagebox.showinfo("No Data", "No invoices found.")
        return

    report_window = tk.Toplevel(root)
    report_window.title("Invoice Report")

    for i, invoice in enumerate(invoices, start=1):
        tk.Label(report_window, text=f"Invoice {i}: {invoice[1]} - ₹{invoice[2]} GST: ₹{invoice[3]}").grid(row=i,
                                                                                                           column=0)


# Button to view invoices
view_button = tk.Button(root, text="View Invoices", command=view_invoices)
view_button.grid(row=4, column=0, columnspan=2)

# Start the Tkinter mainloop
root.mainloop()
```

### 6. `app.py` - Type 2
This is the main Tkinter application file.

```bash
pip install tksheet
```

```python
import tkinter as tk
from tkinter import messagebox
from database import init_db, save_invoice, get_all_invoices
from gst_calculator import calculate_gst
from utils import validate_input
import tksheet

# Initialize the database
init_db()

# Setup Tkinter window
root = tk.Tk()
root.title("GST Filing Software")

# Create the Tkinter widgets
tk.Label(root, text="Customer Name:").grid(row=0, column=0)
customer_name_entry = tk.Entry(root)
customer_name_entry.grid(row=0, column=1)

tk.Label(root, text="Total Amount:").grid(row=1, column=0)
total_amount_entry = tk.Entry(root)
total_amount_entry.grid(row=1, column=1)

tk.Label(root, text="Invoice Number:").grid(row=2, column=0)
invoice_number_entry = tk.Entry(root)
invoice_number_entry.grid(row=2, column=1)


def save_invoice_button():
    customer_name = customer_name_entry.get()
    try:
        total_amount = float(total_amount_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
        return
    invoice_number = invoice_number_entry.get()

    if not validate_input(customer_name, total_amount, invoice_number):
        return

    cgst, sgst, gst_amount = calculate_gst(total_amount)

    # Save the invoice to the database
    save_invoice(customer_name, total_amount, gst_amount, invoice_number, cgst, sgst)

    # Show success message
    messagebox.showinfo("Success", "Invoice saved successfully.")

    # Clear the input fields after saving
    customer_name_entry.delete(0, tk.END)
    total_amount_entry.delete(0, tk.END)
    invoice_number_entry.delete(0, tk.END)


# Button to save invoice
save_button = tk.Button(root, text="Save Invoice", command=save_invoice_button)
save_button.grid(row=3, column=0, columnspan=2)


def view_invoices():
    # Fetch all invoices from the database
    invoices = get_all_invoices()

    if not invoices:
        messagebox.showinfo("No Data", "No invoices found.")
        return

    # Create a new top-level window to display the invoices
    report_window = tk.Toplevel(root)
    report_window.title("Invoice Report")

    # Create the tksheet table widget
    sheet = tksheet.Sheet(report_window, width=1000, height=400)
    sheet.pack()

    # Set column names (headers)
    sheet.headers(["ID", "Customer Name", "Total Amount", "GST Amount", "Invoice Number", "CGST", "SGST"])

    # Prepare data to be displayed (rows from the database)
    data = []
    for invoice in invoices:
        data.append([invoice[0], invoice[1], invoice[2], invoice[3], invoice[4], invoice[5], invoice[6]])

    # Set the data to the sheet
    sheet.set_sheet_data(data)

    # Allow the user to scroll the data if it's large
    sheet.set_column_width(0, 40)
    sheet.set_column_width(1, 200)
    sheet.set_column_width(2, 100)
    sheet.set_column_width(3, 100)
    sheet.set_column_width(4, 150)
    sheet.set_column_width(5, 100)
    sheet.set_column_width(6, 100)


# Button to view invoices
view_button = tk.Button(root, text="View Invoices", command=view_invoices)
view_button.grid(row=4, column=0, columnspan=2)

# Start the Tkinter mainloop
root.mainloop()
```

### 7. Running the Application
1. Navigate to the folder where your project is located.
2. Ensure you have the correct Python environment set up.
3. Run the `app.py` file:

```bash
python app.py
```

### Features of the GST Filing Software
1. **Invoice Management**: Users can input invoice details, and the software will calculate the GST and store the invoice in the database.
2. **View Invoices**: Users can view a list of all stored invoices.
3. **GST Calculation**: The software calculates CGST, SGST, and total GST based on the entered total amount.
4. **Database**: It uses SQLite to store invoice details and can retrieve and display them.

### Optional Improvements
- **Invoice Export**: Add functionality to export invoices as PDF or Excel files.
- **GST Return Filing**: Include a section where users can generate and file GST returns (e.g., GSTR-1, GSTR-3B).
- **Authentication**: Add user authentication (login) to make the application secure.

This code provides a basic structure to get started with a GST filing software. You can expand it by adding more features like reporting, file export, and tax category handling based on your requirements.)
