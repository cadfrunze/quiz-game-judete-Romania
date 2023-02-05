import turtle
from jocul import Robotzelu
from afisare_scor import TabelaScor


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
tabela_scor = TabelaScor()
joc = True


while joc:
    tabela_scor.tablou_len_data()
    robotelu.raspunde()
    screen.update()
    tabela_scor.incercari = robotelu.greseli
    tabela_scor.scor = robotelu.scor
    if tabela_scor.incercari > 0:
        tabela_scor.tablou_scor()























screen.mainloop()