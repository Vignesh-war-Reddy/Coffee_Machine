import turtle as t 
import random

colours = ["red","green", "black","tomato", "orange"]

tim = t.Turtle()

def draw_shape(no_of_sidess):
    angle = 360 / no_of_sidess
    for i in range(no_of_sidess):
        tim.forward(80)
        tim.right(angle)
for shape in range (3 , 11):
    tim.color(random.choice(colours))
    draw_shape(shape)
    