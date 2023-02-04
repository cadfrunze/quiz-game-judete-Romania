import turtle
from jocul import Robotzelu
import pandas as pd

screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Joc interactiv cu enumerarea tuturor judetelor din Romania')
screen.setup(width=1050, height=1000)
imagine = 'Romania_counties_blank_big.gif'
screen.addshape(imagine)
turtle.shape(imagine)
screen.tracer(0)


robotelu = Robotzelu()
joc = True

while joc:
    robotelu.raspunde()
    screen.update()






















screen.mainloop()