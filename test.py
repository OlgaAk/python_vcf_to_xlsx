from tkinter import *
root = Tk()

def Hello(event):
    print("Yet another Hello world")

btn = Button(root, text="Click me", width=30, height=5, bg="white", fg="black")
btn.bind("<Button-1>", Hello)
btn.pack()
root.mainloop()