import turtle
from jocul import Robotzelu
from afisare_scor import TabelaScor
from tkinter import messagebox
import sys

# Configurarea ecranului, de aici se va executa jocul,
# si totodata scorul


screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Joc interactiv cu enumerarea tuturor judetelor din Romania')
screen.setup(width=1050, height=1000, startx=-100, starty=0)
imagine = './files_for_game/Romania_counties_blank_big.gif'
screen.addshape(imagine)
screen.cv._rootwindow.resizable(False, False)
turtle.shape(imagine)
screen.tracer(0)

t = turtle.Turtle()
t.penup()
t.hideturtle()
t.color('red')
t.goto(x=150, y=-340)
t.write(font=('Arial', 8, 'normal'), arg='V.1.0\nPowered by Cadfrunze')
robotelu = Robotzelu()
tabela_scor = TabelaScor()
joc = True

tabela_scor.tablou_len_data()
while joc:
    # Atentie la conditia 'if'...degeaba il scriem mai jos!
    if len(robotelu.ver_raspuns) == 41:
        messagebox.showinfo(title='Felicitari!', message='Ai castigat jocul!')
        joc = False


    elif tabela_scor.incercari == 41:
        messagebox.showerror(title='Dute-n pula!', message='Ai pierdut')
        joc = False

    robotelu.raspunde()
    tabela_scor.verificare = robotelu.check
    tabela_scor.verificare_raspuns()







































messagebox.showinfo(title='Bun venit', message='For other projects:\ngithub.com/cadfrunze\nContact:\nmarius1890@yahoo.com')

screen.mainloop()


