import os
import ctypes
import time
import schedule
from datetime import datetime
from pathlib import Path
import random

# Function to set the wallpaper
def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# Function to get all image paths from a directory
def get_images_from_directory(directory):
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    return [str(p) for p in Path(directory).glob('*') if p.suffix.lower() in supported_formats]

# Function to rotate wallpaper
def rotate_wallpaper(image_directory):
    images = get_images_from_directory(image_directory)
    if not images:
        print("No images found in the specified directory.")
        return
    image_path = random.choice(images)
    print(f"Setting wallpaper to: {image_path}")
    set_wallpaper(image_path)

# Function to schedule wallpaper rotation
def schedule_wallpaper_rotation(directory, interval):
    schedule.every(interval).minutes.do(rotate_wallpaper, image_directory=directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Main function to get user input and start the schedule
def main():
    image_directory = input("Enter the path to your image collection: ").strip()
    if not os.path.exists(image_directory):
        print("The specified directory does not exist.")
        return

    try:
        interval = int(input("Enter the interval in minutes for rotating the wallpaper: ").strip())
    except ValueError:
        print("Please enter a valid number for the interval.")
        return

    print(f"Scheduling wallpaper rotation every {interval} minutes from directory: {image_directory}")
    schedule_wallpaper_rotation(image_directory, interval)

if __name__ == "__main__":
    main()