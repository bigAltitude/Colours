


# Tkinter Color Picker

## Description
This Python script creates a **Tkinter-based color selection tool** that displays a **grid of color buttons**. Users can click on a color to **copy its RGB hex value**, view it in **floating preview windows**, or **copy the color name** with a right-click.

## Features
- **Grid of color buttons** extracted from a compressed dataset.
- **Click to copy** RGB hex values to the clipboard.
- **Right-click to copy** the color name.
- **Two floating preview windows** display the last two selected colors.
- **Non-resizable and fixed-location UI**.
- **Exit with Escape key or middle mouse button**.

## Installation
1. Ensure you have Python 3 installed.
2. Install Tkinter (included in standard Python distributions).
3. Save the script as `color_picker.py`.

## Usage
Run the script:
```sh
python color_picker.py
```
- **Left-click a color** → Copies its RGB hex value.
- **Right-click a color** → Copies its name.
- **Click a preview window** → Copies the displayed color.
- **Press Escape or middle-click** → Closes the app.

## Dependencies
- `Tkinter` (for the GUI)
- `pickle` & `zlib` (for color data storage and compression)

## License
This project is open-source and free to use.


