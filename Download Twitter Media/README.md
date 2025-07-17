# 1 - Introduction

To run this application, you'll need to have the requests, beautifulsoup4, and tkinter libraries installed. You can install them using pip install requests beautifulsoup4 tk.

When you run the application, it will open a window where you can enter the Twitter profile URL and choose the directory where you want to save the downloaded media files. After clicking the "Download" button, it will fetch the HTML content of the profile, extract the media URLs, and download the files to the specified directory.

Please note that this code relies on the specific HTML structure of the Twitter website, so any changes to the website's layout could break the scraping functionality. Additionally, be aware of any legal and ethical considerations when downloading media from Twitter profiles.

```
pip install requests beautifulsoup4 tk
```

# 2 - `app.py`

```
import os
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog


def download_media(url, save_directory):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    media_elements = soup.find_all('div', class_='AdaptiveMedia-photoContainer js-adaptive-photo ')

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for i, media in enumerate(media_elements):
        media_url = media['data-image-url']
        file_extension = media_url.split('.')[-1]
        file_name = f'media_{i}.{file_extension}'
        save_path = os.path.join(save_directory, file_name)

        with open(save_path, 'wb') as file:
            media_response = requests.get(media_url)
            file.write(media_response.content)


def browse_directory():
    directory = filedialog.askdirectory()
    save_directory_entry.delete(0, tk.END)
    save_directory_entry.insert(tk.END, directory)


def download_profile_media():
    profile_url = url_entry.get()
    save_directory = save_directory_entry.get()

    if not profile_url or not save_directory:
        return

    download_media(profile_url, save_directory)
    tk.messagebox.showinfo("Download Complete", "Media files have been downloaded successfully!")


# Create the main window
window = tk.Tk()
window.title("Twitter Profile Media Downloader")

# Create the URL entry
url_label = tk.Label(window, text="Twitter Profile URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Create the save directory entry
save_directory_label = tk.Label(window, text="Save Directory:")
save_directory_label.pack()
save_directory_entry = tk.Entry(window, width=50)
save_directory_entry.pack()

# Create the browse button
browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.pack()

# Create the download button
download_button = tk.Button(window, text="Download", command=download_profile_media)
download_button.pack()

# Start the main loop
window.mainloop()
```