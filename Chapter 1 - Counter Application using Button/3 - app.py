import tkinter as tk

# OOP Style
class CounterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x200")
        self.title("Counter")

        self.count = tk.IntVar()
        self.count.set(0)

        self.create_widgets()

    def create_widgets(self):
        self.value_label = tk.Label(self, textvariable=self.count)
        self.value_label.pack()

        self.increment_text = tk.StringVar()
        self.increment_text.set("+ Increment")
        self.increment_btn = tk.Button(self, textvariable=self.increment_text, command=self.increment)
        self.increment_btn.pack()

        self.decrement_text = tk.StringVar()
        self.decrement_text.set("- Decrement")
        self.decrement_btn = tk.Button(self, textvariable=self.decrement_text, command=self.decrement)
        self.decrement_btn.pack()

        self.reset_text = tk.StringVar()
        self.reset_text.set("RESET")
        self.reset_btn = tk.Button(self, textvariable=self.reset_text, command=self.reset)
        self.reset_btn.pack()

    def increment(self):
        self.count.set(self.count.get() + 1)

    def decrement(self):
        self.count.set(self.count.get() - 1)

    def reset(self):
        self.count.set(0)

if __name__ == "__main__":
    app = CounterApp()
    app.mainloop()
