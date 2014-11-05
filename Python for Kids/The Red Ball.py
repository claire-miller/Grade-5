#
#imports
#
from tkinter import *
import random

import time

#
# Ball class
#
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 246, 100)
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()

    def redefine(self, color):
        pass       

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1

#
# main code
#

tk = Tk()
tk.title('The Red Ball!')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=400, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
ball = Ball(canvas, 'red')

i = 0

while 1:
    i = i + 1

    if i % 100 == 0:
        ball.redefine('green')
        i = 0
        
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.001)
    
    
