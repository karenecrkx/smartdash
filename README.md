# SmartDash

SmartDash is a Python program that automatically rotates your desktop wallpaper on Windows based on a schedule you define. You can specify a collection of images and how often you want the wallpaper to change.

## Features

- Rotate your desktop wallpaper at regular intervals.
- Supports various image formats including JPG, JPEG, PNG, BMP, and TIFF.
- Simple command-line interface to set up your wallpaper schedule.

## Requirements

- Windows operating system
- Python 3.x
- `schedule` package (install via pip)

## Installation

1. Ensure you have Python 3.x installed on your Windows machine.
2. Install the required `schedule` package by running:

   ```
   pip install schedule
   ```

3. Download or clone this repository to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `smartdash.py` is located.
3. Run the program using Python:

   ```
   python smartdash.py
   ```

4. Enter the path to your image collection when prompted.
5. Enter the interval in minutes for how often you want the wallpaper to change.

## Notes

- Ensure the image directory only contains supported image formats to avoid errors.
- The program will continue running until you manually stop it (e.g., via Ctrl+C in the terminal).

## License

This project is licensed under the MIT License. See the LICENSE file for details.