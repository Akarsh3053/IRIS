import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        style = Style()
        style.configure('TButton', font=('Helvetica', 16))

        # Load the background image and icons
        bg_image = Image.open("background.jpg")
        icon1 = Image.open("icon1.png")
        icon2 = Image.open("icon2.png")
        icon3 = Image.open("icon3.png")
        icon4 = Image.open("icon4.png")

        # Create PhotoImage objects
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.icon1_photo = ImageTk.PhotoImage(icon1)
        self.icon2_photo = ImageTk.PhotoImage(icon2)
        self.icon3_photo = ImageTk.PhotoImage(icon3)
        self.icon4_photo = ImageTk.PhotoImage(icon4)

        # Create a canvas and add the background image
        self.canvas = tk.Canvas(self, width=self.bg_photo.width(), height=self.bg_photo.height())
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        # Add the icons to the canvas
        self.canvas.create_image(100, 100, image=self.icon1_photo)
        self.canvas.create_image(200, 100, image=self.icon2_photo)
        self.canvas.create_image(300, 100, image=self.icon3_photo)
        self.canvas.create_image(400, 100, image=self.icon4_photo)

        self.canvas.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
