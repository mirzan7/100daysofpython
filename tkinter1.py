import tkinter as tk
from tkinter import ttk

def convert():
    eur_input = entry_int.get()
    inr_output = eur_input * 90
    output_string.set(inr_output)
 
#window
window = tk.Tk()
window.title('EUR TO INR coverter')
window.geometry('300x150')

#title
text_label = ttk.Label(
    master = window,text ='EUR to INR conveter',
    font='calibri 20 bold')
text_label.pack()

#input
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(
    master = input_frame, 
    textvariable = entry_int)
button = ttk.Button(
    master = input_frame, 
    text = 'convert', 
    command = convert)
entry.pack(side = 'left',padx=10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    font = 'calibri 24',
    textvariable = output_string)
output_label.pack(pady = 5)

#run
window.mainloop()