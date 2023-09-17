import tkinter


def convert_to_km():
    user_input = miles.get()
    kilometer = tkinter.Label(text=f"{int(user_input) * 1.609}")
    kilometer.grid(column=2, row=2)


window = tkinter.Tk()
heading = tkinter.Label(text="Enter the miles to be converted :")
heading.grid(column=0, row=0)

miles = tkinter.Entry(width=10)
miles.size()
# miles.insert('miles')
miles.grid(column=2, row=0)

convert = tkinter.Button(text="Convert", command=convert_to_km)
convert.grid(column=0, row=1)

window.mainloop()
