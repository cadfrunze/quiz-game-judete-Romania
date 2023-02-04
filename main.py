import turtle
import pandas as pd

from test import coordonate
screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Joc interactiv cu enumerarea tuturor judetelor din Romania')
screen.setup(width=1050, height=1000)
imagine = 'Romania_counties_blank_big.gif'
screen.addshape(imagine)
turtle.shape(imagine)
screen.onscreenclick(coordonate)
screen.tracer(0)

new_elem = turtle.Turtle()
new_elem.hideturtle()
new_elem.penup()
new_elem.shapesize(5)
new_elem.goto(x=-400, y=300)

dt = pd.read_csv('judetele_final.csv')
dt = dt.judet
dt = dt.to_list()


for elem in dt:
    new_elem.write(arg=f"{elem}", font=('Arial', 20, 'normal'))
    input('enter')
    new_elem.clear()
    screen.update()


















screen.mainloop()