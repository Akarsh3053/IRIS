from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

# window config
window = tk.Tk()
window.iconbitmap("assets/IRIS.ico")
window.title("IRIS")

window.state('zoomed')


# BG image config
bg_image = Image.open("assets/bg.jpg")
# bg_image = bg_image.resize()
background = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(window, width=background.width(), height=background.height())
canvas.pack()

canvas.create_image(0, 0, image=background, anchor='nw')

# run
window.mainloop()