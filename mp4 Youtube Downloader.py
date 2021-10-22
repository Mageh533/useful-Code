from pytube import YouTube
from pytube.cli import on_progress

url = input("Type the link here: ")
print("Starting download...")
YouTube(url, on_progress_callback=on_progress).streams.get_highest_resolution().download()
