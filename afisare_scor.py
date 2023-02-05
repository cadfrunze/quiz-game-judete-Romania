import turtle
import pandas as pd


# Construirea schemei tabela afisare scor

data = pd.read_csv('./files_for_game/judetele_final.csv')
data = data.judet
data = data.to_list()

class TabelaScor():
    """
    Afisare scor, si numar de incercari
    """

    def __init__(self):
        self.obiect = turtle.Turtle()
        self.obiect.hideturtle()
        self.obiect.penup()
        self.scor = 0
        self.incercari = 0
        self.LEN_DATA = len(data)
        self.modify_len = len(data)

    def tablou_scor(self):
        self.refresh()
        self.obiect.goto(x=-380, y=350)
        self.obiect.color('red')
        self.obiect.write(arg=f'Numar greseli: {self.incercari}', font=('Arial', 15, 'normal'))

    def tablou_len_data(self):
        self.refresh()
        self.modify_len -= self.scor
        self.obiect.goto(x=-280, y=350)
        self.obiect.color('blue')
        self.obiect.write(arg=f'Numar judete ramase: {self.modify_len}| Numar total judete: {self.LEN_DATA}', font=('Arial', 15, 'normal'))

    def refresh(self):
        self.obiect.clear()
