import tkinter as tk

# OOP Style
class CounterApp:
    def __init__(self, master):
        self.master = master
        master.title("Counter")
        master.geometry("300x100")

        self.value = 0

        self.seekbar = tk.Scale(
            master, 
            from_=0, 
            to=10, 
            orient=tk.HORIZONTAL, 
            command=self.on_seekbar_change
        )
        self.seekbar.pack(padx=20, pady=10)

        self.label = tk.Label(
            master, 
            text="Value: {}".format(self.value)
        )
        self.label.pack(pady=5)

    def on_seekbar_change(self, value):
        if int(value) > self.value:
            if self.value < 10:
                self.value += 1
        elif int(value) < self.value:
            if self.value > 0:
                self.value -= 1

        self.seekbar.set(self.value)
        self.label.configure(
            text="Value: {}".format(self.value)
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()