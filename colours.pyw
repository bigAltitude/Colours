#  ┌───────────────────────┐
#  │ -*- coding: utf-8 -*- │
#  │ Author: S. Perkins    │
#  │ Date: 2024-09-02      │
#  └───────────────────────┘

#  ┌──────────────────────────────────────────────────────────┐
#  │ This script creates a Tkinter-based color selection tool │
#  │ with a grid of color buttons. Colors are extracted from  │
#  │ a compressed, pickled list and displayed in a grid.      │
#  │                                                          │
#  │ Clicking a button selects a color, updates two floating  │
#  │ preview windows, and copies the RGB hex value to the     │
#  │ clipboard. Right-clicking a button copies the color name.│ 
#  │                                                          │
#  │ The UI is fixed in size and location, with exit options  │
#  │ via the Escape key or middle mouse button. This tool is  │
#  │ useful for quickly selecting and copying colors.         │
#  └──────────────────────────────────────────────────────────┘

import zlib
import pickle
from tkinter import *

#  ┌────────────────────────────────────┐
#  │ Set the dimensions for the buttons │
#  └────────────────────────────────────┘
tilewidth = 3
tileheight = 2

#  ┌─────────────────────────────────────────────┐
#  │ Set the initial location of the main window │
#  └─────────────────────────────────────────────┘
locationX = 50
locationY = 50

#  ┌─────────────────────────────────────────────────────────────┐
#  │ Define the geometry (size and position) for the main window │
#  └─────────────────────────────────────────────────────────────┘
location = "400x250+1600+100"

#  ┌────────────────────────────────┐
#  │ Compressed list of color names │
#  └────────────────────────────────┘
compressed_colours = (
    b'x\x9cm\x98Ko\xdbF\x10\xc7\x0bTvl\xf9\x95\xa2@\xd1\xa3\x80\xf4\xd0SQ\xce$M\xaeM\x0c\xa4'
    b'\x05\x92\xc6\x88\x8b\x06=\xe4\xb0"\xd7\x12+\x8a\xab\x90\x94\r\xf5\xd4\x0f\xd0c\xfa}\xbb'
    b'\x8f!wvH\x9f\xe6\xf7\xd7\xcc\xee\xec\xec\x93\xfeg\xf6\xdfw\xdf~\xe1\xff>~\xfe\xfe\xe3'
    b'\xe7\x7fgmm\x1e>+k\x9d\xad\xd6\xa6\xed\x16\x0f\xeb\xb2\xd3A\xf0\xe6\xa2\xdd\x9aM\x10N'
    b'W\xaa\xac\xdb\xa5i\x8c\xc7\xf3\xbb\xca4\xaab\x11\'\xa6*\x16\x95\xca\x03\x1dUe\xadko^'
    b'\xa8\xba+?\xed5o}\xa7v\xea\xa0\x9c\xb2\xf3\xc2\xd5\xb2Ru\xbe\xd6\xc5BU[S\x17^<^\x96'
    b'\xad\x8d\xf3\xf6|\xa7U\xbe^\xec\xf6ww\xa1\xffZ\xdd\xab\xbf\x0ck\xf3\xa2\xd26r\x91\xaf'
    b'\xcb\xbb;\x13z\x9eo\xcb\xba[\xe4\x8dV\xdb\x90\x94\xfa{\xdfP{\xaa*s\xbdXV\xd4\xfeI\xa5'
    b'\xeeu]\xe8\xc6\xd3eO\xce\xa1]\xf7\x8d\xb5\xdda\xd1\x986D\\\x15\xaa\xd9,\xdaJ\xd92\xad'
    b'\x1au\x08\xcd\x14\xe56\xd2\\\xfc\xfa\xb8*W\xebN\xc6\xcc\xa2\x7f\xf8}\xd5\xe8\xc0\x17'
    b'\xdb\xb2\xa8\xbd4\xe49\xb3\xe3\x0e?^\xe5\xa6\xa9\xed,<\x84,\xc7I\r\xe2\\\xf0W[]\x94'
    b'\xfb\xadtK\xb2\x1b\xd43r\x8e\xad5\xe6`\'>f\x14]\x0bS\xacx6\x17\x85\xd6\xbbE\xbb9\xb0'
    b":'tI]rm\xdevZW\xe3\xb4R\x95J\x15\xfb\xde\x99\x87\x82\xf7}\xb9S\x95^t\xfb\xe6\xd3\xde"
    b'\x944e\x97\xbe:\xa9\xf6\x98\xc6\x97\xaa\xa7)\xce\xf2\x83\xaay\xbf\x91sU\xe8n\\[\xf5i'
    b'\xaf\xb6\xaa\xb1\x9b\x80\x96\x9b`\x9f\x89\x9dh\xda#\x8f=\x9b\xaa\xbc\xd7L\r\xf9\xb6'
    b'Z1\xed4\xc5>\xfdT\xbd\xa2\x9a%\xe2\xdcW$\xf2y\xbb\xb3\xf9\xac\xb8G\xa5\x1ej\xc6_\xf7'
    b'\x8dK\xc7so.\x0e\xba\xaa\xe8\x00\xb1u\xd9&\x8d\x87\xdf\xb8rg\x1a\xddv\xbc\xbb0\xde\xa2'
    b'QKV\x94\xcdZm\xca\xb0]\xa3\x19fse\x8f\x18]7&\x1c\x0f\xdf\xd0n\xe9E\x9e\xcey\xf8\x8d)'
    b'\xc7\xcc\x9e\xb9\x18^\xa8\xb4\xe1\xd3\x14\xc3,\xa4\x9a\xdd\x04\xad]\xb3\x8dy\xa0\xa1'
    b'\x94uQ\xaaz\xd1\xe8\x82j\xab\x8a\xc2f\x1c=\xceZU\x17<\xe4,L\xae?\xefB\x86\xcc\xa6\xfc'
    b'\xf9\xaf\xf6\xb8\xadW\x9a\x852\xe1(w\x87q\xf8\x8d\x16\xe8 \x1cwf\xab:C\x15\xf71C\x9a'
    b'_\xf6\xc6\xc9\xdat\x8b]YoB\x01\xfc\xbe\x1dp6X\xb4\xfa\x07\xbe\xf2\xd3r_\x9a\xca\xee'
    b'\x81\xbe\xadc\xbb\xce\re\xddo\x07\xe12\x17|An\xa6\xb1\xc7w\x91\x8cQ\x08!0\x08n\xd3q'
    b'\xe1x\xb7ov\x95NZd\xd2\xa3nmOp\x82#w\xf5A41\x9aO\x87}\xd6\xae\xed\x9a\x81\x141\xc5'
    b'\xe0|\xf1s\xb8\xe2>\xb8\xdb(\x1bK0\x96p,\x85\xb6\x1e\x85[\x0f8 \x87\xe06\xbfq\x17'
    b'\xe2\x8d\xbd\x0fA0\n\x0e\xfe\xe7\xbf\xf9\x0b\x93\xa5\xc3\x15\x1c)4\xb07\xeeR}\x15'
    b'\xeeT\x18K8\x96\xa8|\xeevj\xcbj\x03)b\x8a\xc1\xf9\xb8\xbc7\xcd\x01\x98\x8d\xcc\xa6'
    b'\x06\xd7\xa6\xd6\x87B\xd3\xa4\r\x88)\x06\xe7\xcb7t\x7f\xbft\xd77Lh8\xa1Qa\xdf\xba{'
    b'\xfe\xbd\xbd\xe6A0\n\xa6\xe4\xfd\xa3\x02\x98\x8d\xcc\xa66o\xdd\xa5j;\xa1\xc5\x11\x19'
    b'\x04\xa3`\x8a\x7f\xef\xee\\\x16?0\x08F\xc1!\xfeh9\xb8z3\xa8g\xd7\xfe\xbe\x8e\xcd0\x01'
    b'\xa5\xd0\x0f\xc4]\xc3| =\x83`\x14L\xab\xf0\xda\x9e,\xb7\x9bC\x8c\xe0\n\x8e\x94\x10u'
    b'B\x94%\x04\taB\xfd\xeau\xc7U\x12\x9cH0\x96p,\xf1)|m\x9fj\x99`\x10\x8c\x82C\xfcUh2'
    b'-\x9f\x10aJ\xc4)\x91r\xf2"\x9b\x8d\x81A0\n\xe6\xf1\xaf\xec[\x06\x04\xa3`\xdaV7\xf6'
    b'\xb8\xff\xbd\x7f\x19e\x13\x1aLh8\xa1Q\xff\xaf\xdc\xe3\x89\xe5?0\x08F\xc1\x14\xdf\xa5'
    b'\xb9D\x06\xc1(\x98\xb6E>\x0c\xdd\x9b\x18M\x1a\xf0\xb5\xbds\xc4\xc4\xa7\x1aLh8\xa1'
    b'\xd1\x8e\x8b\xcf@\x90\x02-Y\x1f\xa5\xd5k\xf7J\xca\xc6\x12\x8c%\x1cKtd\xa6\xed\x9c'
    b'\xa6m\x9c\xa6\xf1s7?\xcc;2\x08\x96\xfe\xb4\xb3o\xfd#\x91Ep\x05G\n\x1d\x9e\xab\xe8'
    b'\x1fld6\x15-_\xab\xa6k\xf4\xbe\x9fV&\xa0\x14ha\xbcs/\xcbk\xfb\xb0\xcc\x04\x83`\xda'
    b'\x9c\xaex^c\x15\x10"L\x898%\xd2\xd0\xfc\xeb5c60\x1b\x99\xcd\x0f\x88\xd7\xfd33\x9b'
    b'\x12aJ\xc4)\x91&\xc5\x8b\x7f\xfa\x97/\x8c\x14\x1c)\xf4\x029\xb0\x00\x02\xe4@\xbb'
    b'\xc7=\x89!\x9a\x18M\x9a\x85U:\x98\xc8 \x18\x05\xb3\xdd\'\n\x92j0\xa1\xe1\x846\xdc'
    b'\xa2\xed\xe1\xa5{\x80g\x82A0\n\xa6\xf8_\xfd#\xff\xbd\xee\xc730\x08F\xc1T\xd7\xb6'
    b'\xd4u\xad2\x0e\xc0\x019P\x9f\xcb}S\x1d\x1e\xccP\xc3\x81A0\n\xa6U\xf8\xb0\xd6\xaa'
    b'\xcb\x98\r\xccFf\x07\xffY\xa7\xa8:\xce\x82\xc1\xa2l\xf2\xb5\xc9\x8d;\xd32\xc1 \x98'
    b'\xb2\xb9+\x1b\xbdl\xca|\x93\t\x06\xc1\xd2\x9f\xb2_\xc6\xd9\n60\x1b\x99\xddW\xd8'
    b'\x7f0e\x1c\x80\x03r\xe0{\xe4\x96\xf9r\x05G\n\xf5\x14\xbe\xa4\x80\x03r\xe8\x9fX\xee'
    b'd\xf0B&\x05\x90\x02J\x81\x8a\xe0\xbf\xe52f\x03\xb3\x91\xd9\x94Z\xf8\xe0\x03\x0e\xc8'
    b'\xa1?#}\x1fq\xf5\x0e\x8c\x82ie4\xbd\xa7\xb3p\xb0\xe8\xaeq\x8f\xb6\x1b\xfb]\x08)b\x8a'
    b'\xf4\x9e\xfb\xc5t\x8e\xb2\x84 !L\x88N\x9c\xdd\x10\xe4M\x88&F\x93\xbfmb/\x91A0\nfo'
    b'\x9d?\xfc\xc7\xe5\xb0\xe1S\r&4\x9c\xd0hV\xc2Wq\xc6\x018 \x07\x1a\x83\xe8\x7f.\xfa'
    b'\x9e\x8b~\xe7\xa2\xcf\x93\xadZ\xe9\xba\xa3C\xa6\'LhX\xce\xeeC;\xe3\x00\x1c\x90C?\x1b'
    b'\xd5~\x9bE\x13\xa2\x89\xd1\xa4g\xcd[\xff9\xfe\x8e\xf5\x92H0\x96p,%{*\xb6\xc4\x04'
    b'\x90\x02J\x81\xc6\x1b\xfe/\x90q\x00\x0e\xc8!\x19\xc3\r\x8bL$\x18K8\x96hf\xe8\x7f'
    b'\x11YB\x90\x10&D5\x7fY\xa9<\xfc\xef\xe5\xd8\xfd\xdb\x18\x9eE\xfb\xa7\x9f\xa2\xfd'
    b'\xec\xc7h?\x0f>G\x1f\x86\x7f\x95?z\x02/\xb2\xa7\x19\x95\xe2\xc9s\xcc^d/\x08\xf2'
    b'\x0c\x9e\x82\xfdE\xff\xf0?^&\x8a\xe9'
)
colours = pickle.loads(zlib.decompress(compressed_colours))

#  ┌───────────────────────────────────────────────────────────────────────┐
#  │ Function to handle the selection of a color and display its RGB value │
#  └───────────────────────────────────────────────────────────────────────┘
def run(index):
    selected_colour = programlist[index][0]
    rgb_value = root.winfo_rgb(selected_colour)
    rgb_value = "{:02x}{:02x}{:02x}".format(rgb_value[0] // 256, rgb_value[1] // 256, rgb_value[2] // 256)
    root.clipboard_clear()
    root.clipboard_append(rgb_value)
    print(selected_colour, rgb_value)
    colour2.set(colour1.get())
    colour1.set(selected_colour)
    waitwindow1.config(background=selected_colour)
    waitwindow1.update()
    waitwindow2.config(background=colour2.get())
    waitwindow2.update()
    return

#  ┌──────────────────────────────────────────────────────────────────┐
#  │ Function to copy the name of the selected color to the clipboard │
#  └──────────────────────────────────────────────────────────────────┘
def copy_name(index):
    selected_colour = programlist[index][0]
    root.clipboard_clear()
    root.clipboard_append(selected_colour)
    print("Copied to clipboard:", selected_colour)

#  ┌────────────────────────────────────────────────────────────┐
#  │ Function to copy the first selected color to the clipboard │
#  └────────────────────────────────────────────────────────────┘
def copy_colour1(event):
    root.clipboard_clear()
    root.clipboard_append(colour1.get())
    print("Copied to clipboard:", colour1.get())

#  ┌─────────────────────────────────────────────────────────────┐
#  │ Function to copy the second selected color to the clipboard │
#  └─────────────────────────────────────────────────────────────┘
def copy_colour2(event):
    root.clipboard_clear()
    root.clipboard_append(colour2.get())
    print("Copied to clipboard:", colour2.get())

#  ┌───────────────────────────────────────────────────────────────────┐
#  │ Create the program list and populate it with colors and positions │
#  └───────────────────────────────────────────────────────────────────┘
programlist = []
cnum = 0
clistlen = len(colours)

for i in range(20):
    for j in range(30):
        cnum += 1
        if cnum < clistlen:
            programlist.append([colours[cnum][0], i, j, colours[cnum][0]])

#  ┌───────────────────────────────────┐
#  │ Function to close the main window │
#  └───────────────────────────────────┘
def callback(func=None):
    root.destroy()

#  ┌────────────────────────────────────┐
#  │ Initialize the main Tkinter window │
#  └────────────────────────────────────┘
root = Tk()

#  ┌──────────────────────────────────────────────────┐
#  │ Variables to store the currently selected colors │
#  └──────────────────────────────────────────────────┘
colour1 = StringVar()
colour2 = StringVar()

colour1.set("DarkSeaGreen4")
colour2.set("DarkSeaGreen1")

#  ┌────────────────────────────────────────────────────┐
#  │ Set the geometry and properties of the main window │
#  └────────────────────────────────────────────────────┘
root.geometry("+" + str(locationX) + "+" + str(locationY))
root.overrideredirect(True)
root.resizable(False, False)
root.bind("<Button-2>", callback)
root.bind("<Escape>", callback)

#  ┌──────────────────────────────────────────────────────────┐
#  │ Create buttons for each color and place them on the grid │
#  └──────────────────────────────────────────────────────────┘
button = []

for pointer, title in enumerate(programlist):
    btn = Button(root, command=lambda x=pointer: run(x),
                 width=tilewidth,
                 height=tileheight,
                 bg=title[0],
                 font='"Lucida Console" 8',
                 anchor='center',
                 fg='Black'
                 )
    btn.grid(row=title[1], column=title[2])
    btn.bind("<Button-3>", lambda event, x=pointer: copy_name(x))
    button.append(btn)

#  ┌──────────────────────────────────────────────────────────────────┐
#  │ Create the first wait window to display the first selected color │
#  └──────────────────────────────────────────────────────────────────┘
waitwindow1 = Toplevel(root)
waitwindow1.geometry("180x180+200+450")
waitwindow1.overrideredirect(True)
waitwindow1.resizable(False, False)
waitwindow1.config(padx=5,
                   pady=5,
                   relief='raised',
                   borderwidth=2,
                   background=colour1.get())

#  ┌────────────────────────────────────────────────────────────────────┐
#  │ Create the second wait window to display the second selected color │
#  └────────────────────────────────────────────────────────────────────┘
waitwindow2 = Toplevel(root)
waitwindow2.geometry("180x180+437+450")
waitwindow2.overrideredirect(True)
waitwindow2.resizable(False, False)
waitwindow2.config(padx=5,
                   pady=5,
                   relief='raised',
                   borderwidth=2,
                   background=colour2.get())

#  ┌──────────────────────────────────────────────────────────┐
#  │ Entry field to display and edit the first selected color │
#  └──────────────────────────────────────────────────────────┘
msg1 = Entry(waitwindow1,
             textvariable=colour1,
             width=15,
             bg='White',
             fg='Black',
             relief='sunken', borderwidth=3,
             font=("Consolas 14")).grid(row=1,
                                       column=0)

#  ┌───────────────────────────────────────────────────────────┐
#  │ Entry field to display and edit the second selected color │
#  └───────────────────────────────────────────────────────────┘
msg2 = Entry(waitwindow2,
             textvariable=colour2,
             width=15,
             bg='White',
             fg='Black',
             relief='sunken', borderwidth=3,
             font=("Consolas 14")).grid(row=1,
                                       column=1)

#  ┌──────────────────────────────────────┐
#  │ Bind events to the first wait window │
#  └──────────────────────────────────────┘
waitwindow1.bind("<Escape>", callback)
waitwindow1.bind("<Button-2>", callback)
waitwindow1.bind("<Button-1>", copy_colour1)

#  ┌───────────────────────────────────────┐
#  │ Bind events to the second wait window │
#  └───────────────────────────────────────┘
waitwindow2.bind("<Escape>", callback)
waitwindow2.bind("<Button-2>", callback)
waitwindow2.bind("<Button-1>", copy_colour2)

#  ┌─────────────────────────────┐
#  │ Start the Tkinter main loop │
#  └─────────────────────────────┘
root = mainloop()
