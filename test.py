
 
def show_message():
    messagebox.showinfo("GUI Python", message.get())

def quit():
    root.quit()
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

text = Label(width=25, height=5, )
text['text']="Just a text Widget\nin two lines\n"
text.pack()
 
message_button = Button(text="Ok", command=show_message)
message_button.place(relx=.8, rely=.8, anchor="c")

message_button = Button(text="Exit", command=quit)
message_button.place(relx=.9, rely=.8, anchor="c")
 
root.mainloop()