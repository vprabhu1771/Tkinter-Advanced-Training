import tkinter as tk

# Without OOP Style
def on_seekbar_change(value):
    value = int(value)  # Convert value to an integer
    if value > seekbar.get():
        if seekbar.get() < 10:
            value += 1
    elif value < seekbar.get():
        if seekbar.get() > 0:
            value -= 1

    seekbar.set(value)
    label.configure(text="Value: {}".format(value))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Counter")
    root.geometry("300x100")

    value = 0

    seekbar = tk.Scale(
        root,
        from_=0,
        to=10,
        orient=tk.HORIZONTAL,
        command=on_seekbar_change
    )
    seekbar.pack(padx=20, pady=10)

    label = tk.Label(
        root,
        text="Value: {}".format(value)
    )
    label.pack(pady=5)

    root.mainloop()
