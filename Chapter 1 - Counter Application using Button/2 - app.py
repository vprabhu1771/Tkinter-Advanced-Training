import tkinter as tk

# Without OOP Style
root = tk.Tk()

root.geometry("300x200")

root.title("Counter")

count = tk.IntVar()
count.set(0)

increment = lambda: count.set(count.get() + 1)
decrement = lambda: count.set(count.get() - 1)
reset = lambda: count.set(0)

value_label = tk.Label(root, textvariable=count)
value_label.pack()

increment_text = tk.StringVar()
increment_text.set("+ Increment")
increment_btn = tk.Button(root, textvariable=increment_text, command=increment)
increment_btn.pack()

decrement_text= tk.StringVar()
decrement_text.set("- decrement")
decrement_btn = tk.Button(root, textvariable=decrement_text, command=decrement)
decrement_btn.pack()

reset_text = tk.StringVar()
reset_text.set("RESET")
reset_btn = tk.Button(root, textvariable=reset_text, command=reset)
reset_btn.pack()

root.mainloop()