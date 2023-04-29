import tkinter


def calculate():
    miles = float(miles_entry.get())
    res = round(miles * 1.609, 2)
    result.config(text=f"{res}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=5)
window.config(padx=20, pady=20)

miles_entry = tkinter.Entry(width=20)
miles_entry.grid(column=1, row=0)

miles = tkinter.Label(text='Miles', font=("Arial", 14, 'normal'))
miles.grid(column=3, row=0)

is_equal = tkinter.Label(text="Is equal to", font=("Arial", 14, 'normal'))
is_equal.grid(column=0, row=1)

result = tkinter.Label(text=0)
result.grid(column=1, row=1)

km = tkinter.Label(text='Km', font=("Arial", 14, 'normal'))
km.grid(column=2, row=1)

calculate = tkinter.Button(text='Calculate', command=calculate)
calculate.grid(column=1, row=2)

window.mainloop()
