In Tkinter, you can use the `bind` method to attach an event to a widget. Events can include keypresses, mouse actions, and more. Below is a list of common events you can bind to in Tkinter:

### **Common Events to Bind**
1. **Mouse Events**  
   - `<Button-1>`: Left mouse button click
   - `<Button-2>`: Middle mouse button click
   - `<Button-3>`: Right mouse button click
   - `<Double-Button-1>`: Double-click with the left mouse button
   - `<B1-Motion>`: Mouse drag with the left button pressed
   - `<Motion>`: Mouse movement
   - `<Enter>`: Mouse enters a widget
   - `<Leave>`: Mouse leaves a widget
   - `<MouseWheel>`: Scroll wheel (on Windows)

2. **Keyboard Events**  
   - `<Key>`: Any key press
   - `<KeyPress-A>`: Pressing the "A" key
   - `<KeyRelease-A>`: Releasing the "A" key
   - `<Shift_L>`: Left shift key
   - `<Control_L>`: Left control key
   - `<Alt_L>`: Left alt key
   - `<Escape>`: Escape key
   - `<Return>`: Enter key
   - `<Tab>`: Tab key
   - `<BackSpace>`: Backspace key
   - `<Delete>`: Delete key
   - `<Up>`: Up arrow key
   - `<Down>`: Down arrow key
   - `<Left>`: Left arrow key
   - `<Right>`: Right arrow key

3. **Focus Events**  
   - `<FocusIn>`: Widget gains focus
   - `<FocusOut>`: Widget loses focus

4. **Window Events**  
   - `<Configure>`: Window size or position changes
   - `<Expose>`: Widget needs to be redrawn
   - `<Unmap>`: Widget becomes invisible
   - `<Map>`: Widget becomes visible
   - `<Destroy>`: Widget is destroyed
   - `<Activate>`: Window is activated
   - `<Deactivate>`: Window is deactivated

5. **Other Events**  
   - `<Enter>`: Mouse enters a widget
   - `<Leave>`: Mouse leaves a widget
   - `<Visibility>`: Widget visibility changes

---

### **Example Code**
```python
import tkinter as tk

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

def on_click(event):
    print(f"Mouse clicked at {event.x}, {event.y}")

def on_focus(event):
    print("Widget gained focus!")

# Create the main window
root = tk.Tk()
root.geometry("300x200")

# Create a button
button = tk.Button(root, text="Click Me")
button.pack(pady=20)

# Bind events
root.bind("<KeyPress>", on_key_press)  # Key press event
button.bind("<Button-1>", on_click)  # Left mouse click
button.bind("<FocusIn>", on_focus)  # Focus in event

# Start the main loop
root.mainloop()
```

---

### **Finding the List of Bindable Events**
If you're looking for a comprehensive list of events, you can use the `bind_all` method combined with debugging to capture all events:

```python
import tkinter as tk

def print_event(event):
    print(f"Event: {event}")

root = tk.Tk()
root.bind_all("<Any-KeyPress>", print_event)  # Capture all keypresses
root.bind_all("<Any-Mouse>", print_event)    # Capture all mouse actions

root.mainloop()
``` 

This will print every event triggered, allowing you to explore more possibilities.