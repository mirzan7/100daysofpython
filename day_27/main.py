import tkinter

window = tkinter.Tk()
window.title("My first tkinter program")
window.minsize(500, 300)
text_label = tkinter.Label(text="my name is mirzan")
text_label.pack()


def clicked():
    user_input = enter_input.get()
    text_label["text"] = user_input


enter_input = tkinter.Entry(width=50)

button = tkinter.Button(text="click me", command=clicked)

button.pack()
enter_input.pack()


window.mainloop()
