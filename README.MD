
# Color Picker Tool

A simple **Tkinter-based color selection tool** that allows users to select colors from a grid, copy their RGB hex values or names, and view the last two selected colors in separate preview windows.

## Features

- **Grid of color buttons**: Click a button to select a color.
- **Copy RGB Hex Values**: Left-clicking a color button copies its RGB hex value to the clipboard.
- **Copy Color Names**: Right-clicking a color button copies its name to the clipboard.
- **Preview Windows**: Displays the last two selected colors.
- **Copy Selected Colors**:
  - Left-click the preview windows to copy the displayed color name.
- **Quick Exit**: Right-click (`Button-2`) or press `Esc` to close the application.

## Usage

### Running the Script
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/color-picker-tool.git
   ```
2. Navigate to the directory:
   ```sh
   cd color-picker-tool
   ```
3. Run the script:
   ```sh
   python color_picker.py
   ```

### Controls
| Action | Effect |
|--------|--------|
| **Left-click a color button** | Sets it as the current color and copies its RGB hex value to the clipboard. |
| **Right-click a color button** | Copies the color name to the clipboard. |
| **Left-click a preview window** | Copies the displayed color name to the clipboard. |
| **Right-click or press `Esc`** | Closes the application. |

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)


## License
This project is licensed under the **CC License**.


# Global Screen Pixel Color Picker (Multi-Click)

This tool lets you click anywhere on your screen to grab the HEX color of the pixel you selected. The color value is instantly copied to your clipboard, and a small info window updates with the pixel's coordinates and its HEX code—displayed in the very color you picked. 

## Features

- **Global Color Picking:** Click anywhere on your screen—even outside the app's own window.
- **Real-Time Feedback:** The info window updates with the HEX code and changes its text color to match.
- **Clipboard Integration:** Your picked color's HEX code is automatically copied.
- **Multi-Click Operation:** Keep selecting colors until you press `Esc` to exit.

## Requirements

- **Python 3.x**
- **Pillow**: For taking screenshots  
  Install with: `pip install pillow`
- **pyperclip**: For clipboard handling  
  Install with: `pip install pyperclip`

## How It Works

1. **Fullscreen Overlay:** A nearly invisible fullscreen Tkinter window captures your click.
2. **Screenshot & Processing:** The app hides its windows briefly and takes a screenshot of your entire screen, ensuring it captures only the content behind the overlay.
3. **Color Extraction:** It then extracts the pixel color from the screenshot based on your click's global screen coordinates.
4. **Feedback:** The HEX code is displayed in a small, always-on-top info window and copied to your clipboard.
5. **Repeatable:** Continue clicking to select new colors until you press `Esc` to exit.

## Installation & Usage

1. **Install Dependencies:**

   ```bash
   pip install pillow pyperclip
   ```

2. **Run the Script:**

   ```bash
   python get-colour.py
   ```

3. **Usage:**
   - Click anywhere on your screen to capture the pixel's color.
   - The info window will display the pixel’s coordinates and the HEX code in that color.
   - Press `Esc` to exit the application.

## Troubleshooting

- **Incorrect Color Captured:**  
  If the displayed color seems off (e.g., picking the overlay's color instead of the background), try increasing the delay in the code (`root.after(250, ...)`) to give the OS time to redraw the screen without the overlay.

- **Exit Errors:**  
  A guard mechanism is in place to prevent multiple exit calls. If you experience errors when exiting, ensure you're only pressing `Esc` once.

## License

This project is provided as-is. Use it freely to enhance your color-picking workflow!


