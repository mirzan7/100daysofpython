import tkinter

window = tkinter.Tk()
window.title("My first tkinter program")
window.minsize(500, 300)
text_label = tkinter.Label(text= "my name is mirzan")
text_label.pack()

window.mainloop()