from tkinter import*
root = Tk()
root.title("Tk example")
root.geometry("500x500")
Button(root, text="Button").place(x=100, y=100)
Label(root, text="label").place(x=200, y=100)
root.mainloop()