from tkinter import *
from functools import partial

canvas_width = 500
canvas_height = 400
brush_size = 3
color = "black"


# function for start painting
def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    window.create_oval(x1, y1, x2, y2,
                       fill=color, outline=color)


def draw_rectangle():
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    window.create_rectangle(x1, y1, x2, y2,
                            fill=color, outline=color)


# change size of brush
def change_brush_size(new_size):
    global brush_size
    brush_size = new_size


# change brush color
def change_color(new_color):
    global color
    color = new_color


root = Tk()
root.title('Paint with Python')

window = Canvas(root,
                width=canvas_width,
                height=canvas_height,
                bg='white')

frame = Frame(root)
window.bind("<B1-Motion>", paint)

# select color of line
red_button = Button(bg="red", width=2,
                    command=lambda: change_color("red"))
blue_button = Button(bg="blue", width=2,
                     command=lambda: change_color("blue"))
black_button = Button(bg="black", width=2,
                      command=lambda: change_color("black"))
gray_button = Button(bg="gray", width=2,
                     command=lambda: change_color("gray"))
white_button = Button(bg="white", width=2,
                      command=lambda: change_color("white"))
orange_button = Button(bg="orange", width=2,
                       command=lambda: change_color("orange"))
yellow_button = Button(bg="yellow", width=2,
                       command=lambda: change_color("yellow"))
green_button = Button(bg="green", width=2,
                      command=lambda: change_color("green"))
pink_button = Button(bg="pink", width=2,
                     command=lambda: change_color("pink"))
purple_button = Button(bg="purple", width=2,
                       command=lambda: change_color("purple"))
clear_all_button = Button(text="Clear all", width=10,
                          command=lambda: window.delete("all"))

# select brush size
five_button = Button(text='5', width=2,
                     command=lambda: change_brush_size(5))
seven_button = Button(text='7', width=2,
                      command=lambda: change_brush_size(7))
nine_button = Button(text='9', width=2,
                     command=lambda: change_brush_size(9))
eleven_button = Button(text='11', width=2,
                       command=lambda: change_brush_size(11))
thirteen_button = Button(text='13', width=2,
                         command=lambda: change_brush_size(13))
three_button = Button(text='3', width=2,
                      command=lambda: change_brush_size(3))

window.grid(row=3, column=0,
            columnspan=7, padx=10,
            pady=10, sticky=E + W + S + N)
window.columnconfigure(9, weight=1)
window.rowconfigure(3, weight=1)

red_button.grid(row=0, column=0)
blue_button.grid(row=0, column=1)
black_button.grid(row=0, column=2)
gray_button.grid(row=0, column=3)
white_button.grid(row=0, column=4)
orange_button.grid(row=1, column=0)
yellow_button.grid(row=1, column=1)
green_button.grid(row=1, column=2)
pink_button.grid(row=1, column=3)
purple_button.grid(row=1, column=4)

three_button.grid(row=0, column=5)
five_button.grid(row=0, column=6)
seven_button.grid(row=0, column=7)
nine_button.grid(row=1, column=5)
eleven_button.grid(row=1, column=6)
thirteen_button.grid(row=1, column=7)
clear_all_button.grid(row=0, column=8, sticky=W)

root.mainloop()
