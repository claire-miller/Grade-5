import turtle
sides = 300
kitty = 0.5    
#something else = turtle.Sh
t = turtle.RawPen()
for x in range(0, sides):
    #t.right(360/sides)
    t.circle(25)
    t.circle(kitty)    
    kitty = kitty + 0.5
