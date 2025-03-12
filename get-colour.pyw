# -*- coding: utf-8 -*-
#  ╭───────────────────────────────────────────────────────────╮
#  │                                                           │
#  │ Global Screen Pixel Color Picker (Multi-Click)            │
#  │ Author: S Perkins                                         │
#  │ Company: Geo Consulting Limited                           │
#  │ Date: 2025-03-11                                          │
#  │ Description: Click anywhere on your screen to pick the    │
#  │ pixel's HEX color (copied to clipboard). The info display │
#  │ updates with each click until you press Esc, and the text │
#  │ color becomes the color you picked.                       │
#  │                                                           │
#  ╰───────────────────────────────────────────────────────────╯

import tkinter as tk
from PIL import ImageGrab
import pyperclip

#  ╭──────────────────────────────────────────╮
#  │ Guard to ensure exit_all only runs once. │
#  ╰──────────────────────────────────────────╯
exiting = False

def process_click(x, y):
    try:
        #  ╭───────────────────────────────────────────────────────╮
        #  │ Capture the full screen after our windows are hidden. │
        #  ╰───────────────────────────────────────────────────────╯
        scr = ImageGrab.grab()
        pixel = scr.getpixel((x, y))
    except Exception as e:
        info_label.config(text=f"Error: {e}")
        root.deiconify()
        info_win.deiconify()
        return
    hex_color = "#{:02X}{:02X}{:02X}".format(*pixel)
    info_label.config(text=f"Color at ({x}, {y}): {hex_color}",
                      fg=hex_color)
    pyperclip.copy(hex_color)
    #  ╭────────────────────────────────────────────╮
    #  │ Bring back the windows for the next click. │
    #  ╰────────────────────────────────────────────╯
    root.deiconify()
    info_win.deiconify()

def on_click(event):
    #  ╭────────────────────────────────╮
    #  │ Use global screen coordinates. │
    #  ╰────────────────────────────────╯
    x, y = event.x_root, event.y_root
    #  ╭───────────────────────────────────────────────────────────╮
    #  │ Hide our windows so they don't show up in the screenshot. │
    #  ╰───────────────────────────────────────────────────────────╯
    root.withdraw()
    info_win.withdraw()
    root.update_idletasks()
    #  ╭───────────────────────────────────────╮
    #  │ Increase delay to allow OS to redraw. │
    #  ╰───────────────────────────────────────╯
    root.after(250, lambda: process_click(x, y))

def exit_all(event):
    global exiting
    if exiting:
        return
    exiting = True
    try:
        info_win.destroy()
    except tk.TclError:
        pass
    try:
        root.destroy()
    except tk.TclError:
        pass

#  ╭──────────────────────────────────────────────────╮
#  │ Fullscreen transparent window to capture clicks. │
#  ╰──────────────────────────────────────────────────╯
root = tk.Tk()
root.overrideredirect(True)
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.geometry(f"{screen_w}x{screen_h}+0+0")
root.attributes("-alpha", 0.01)
root.bind("<Button-1>", on_click)
root.bind("<Escape>", exit_all)

#  ╭─────────────────────────────────────────────────────╮
#  │ A small always-on-top window to display click info. │
#  ╰─────────────────────────────────────────────────────╯
info_win = tk.Toplevel(root)
info_win.title("Color Info")
info_win.geometry("300x50+10+10")
info_win.attributes("-topmost", True)
info_label = tk.Label(info_win,
    text="Click anywhere to pick a color.\nPress Esc to exit.",
    font=("Arial", 12), bg="white", fg="black")
info_label.pack(expand=True, fill="both")
info_win.bind("<Escape>", exit_all)

print("Ready! Click anywhere to pick a color. Press Esc to exit.")
root.mainloop()
