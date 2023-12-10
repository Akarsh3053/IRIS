import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# window
window = tk.Tk()
window.title("IRIS")

bg_image = Image.open("bg.png")
bg_image = bg_image.resize()
background = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(window, width=background.width(), height=background.height())
canvas.pack()

canvas.create_image(0, 0, image=background, anchor='nw')

# run
window.mainloop()