

# Global Screen Pixel Color Picker (Multi-Click)

This tool lets you click anywhere on your screen to pick the pixel's HEX color. It copies the HEX value to your clipboard and displays it in a small window—whose text color changes to match the picked color. No more tedious “OK” clicks!

## Features

- **Global Capture**: Click anywhere on your screen.
- **Real-time Feedback**: Displays the HEX color value and updates the label's text color.
- **Clipboard Integration**: The HEX color is automatically copied.
- **Multi-Click Operation**: Continue picking colors until you hit `Esc` to exit.

## Requirements

- Python 3.x
- [Pillow](https://pillow.readthedocs.io/) (`pip install pillow`)
- [pyperclip](https://pypi.org/project/pyperclip/) (`pip install pyperclip`)

## How It Works

1. A nearly invisible fullscreen Tkinter window captures your click.
2. The script hides its own windows and takes a screenshot.
3. It then retrieves the pixel color at the global coordinates where you clicked.
4. The HEX value is shown in a small always-on-top window and copied to the clipboard.
5. You can keep clicking to pick new colors until you press `Esc` to exit.

## Installation & Usage

1. **Install dependencies:**

    ```bash
    pip install pillow pyperclip
    ```

2. **Run the script:**

    ```bash
    python get-colour.py
    ```

3. **Use:**
   - Click anywhere on your screen to pick a color.
   - The HEX value of the pixel will display and copy to your clipboard.
   - Press `Esc` to exit.


## Troubleshooting

- **Incorrect Color Capture:**  
  If you're getting the wrong color (e.g., the color of your tool's window instead of the underlying window), try increasing the delay in the `root.after` call. This ensures the OS has time to fully redraw the screen without the overlay.

- **Exit Errors:**  
  A guard variable prevents multiple destruction calls. If you see errors during exit, ensure you’re only pressing `Esc` once.

## License

This project is provided as-is. Enjoy picking your colors with no fuss!

