To achieve this in Tkinter, you can use the `requests` library to make an HTTP request to the JSONPlaceholder API and then update the title of the Tkinter window with the status code. Here's a simple example to get you started:

```python
import tkinter as tk
import requests

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("HTTP Request Status Display")

        self.status_label = tk.Label(root, text="Status Code: ")
        self.status_label.pack(pady=10)

        self.fetch_button = tk.Button(root, text="Make Request", command=self.make_request)
        self.fetch_button.pack(pady=10)

    def make_request(self):
        try:
            # Make an HTTP GET request to JSONPlaceholder
            response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

            # Update the status label with the status code
            status_code = response.status_code
            self.status_label.config(text=f"Status Code: {status_code}")

            # Optionally, display the response content
            # print(response.json())

        except requests.RequestException as e:
            # Handle request exceptions (e.g., connection error)
            self.status_label.config(text=f"Request Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
```

This example creates a simple Tkinter window with a label displaying the current status code and a button to trigger the HTTP request. The `make_request` method is called when the button is pressed, and it uses the `requests.get` method to make an HTTP GET request to the JSONPlaceholder API. The status code is then displayed in the Tkinter window.

Note: Make sure to install the `requests` library before running the code by using the following command:

```bash
pip install requests
```