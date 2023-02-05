import turtle
from jocul import Robotzelu


# Configurarea ecranului, de aici se va executa jocul,
# si totodata scorul


screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Joc interactiv cu enumerarea tuturor judetelor din Romania')
screen.setup(width=1050, height=1000)
imagine = './files_for_game/Romania_counties_blank_big.gif'
screen.addshape(imagine)
turtle.shape(imagine)
screen.tracer(0)


robotelu = Robotzelu()
joc = True

while joc:
    robotelu.raspunde()
    screen.update()






















screen.mainloop()