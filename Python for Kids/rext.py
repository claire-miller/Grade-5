from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

colorchooser.askcolor()
def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill = fill_color)

random_rectangle(400, 400, '#ffa800')
c = colorchooser.askcolor()
random_rectangle(400, 400, c[2])
    
