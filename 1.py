import turtle
from math import *
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)       # This is new
size = 1
angle=90
def draw_rect():
    tess.forward(size)
    tess.left(90)
    tess.forward(size)

while(1):
   # Leave an impression on the canvas      # Increase the size on every iteration
   draw_rect()
   size+=10# Move tess along
   angle+=0.01
   tess.left(angle)
wn.mainloop()