#it's working!


from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
#Yay!
my_image = PhotoImage(file ='c:\\temp\\pinkie.gif')
#my_image = PhotoImage(file = 'C:\\Users\\Claire\\Desktop\\test.gif')
canvas.create_image(0,0, anchor = NW, image = my_image) 

