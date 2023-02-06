import turtle
import pandas as pd


# Construirea schemei tabela afisare scor

data = pd.read_csv('./files_for_game/judetele_final.csv')
data = data.judet
data = data.to_list()


class TabelaScor:
    """
    Afisare scor, si numar de incercari
    """

    def __init__(self):
        self.obiect = turtle.Turtle()
        self.obiect1 = turtle.Turtle()
        self.obiect1.hideturtle()
        self.obiect1.penup()
        self.obiect.hideturtle()
        self.obiect.penup()
        self.LEN_DATA = len(data)
        self.modify_len = len(data)
        self.verificare = None
        self.incercari = 0

    def tablou_scor(self):
        self.refresh_scor()
        self.obiect.goto(x=-500, y=250)
        self.obiect.color('red')
        self.obiect.write(arg=f'Numar greseli: {self.incercari}', font=('Arial', 15, 'normal'))

    def tablou_len_data(self):
        self.refresh_len_data()
        self.obiect1.goto(x=-350, y=330)
        self.obiect1.color('blue')
        self.obiect1.write(arg=f'Numar judete ramase: {self.modify_len}| Numar total judete: {self.LEN_DATA}',
                           font=('Arial', 15, 'normal'))

    def refresh_len_data(self):
        self.obiect1.clear()

    def refresh_scor(self):
        self.obiect.clear()

    def verificare_raspuns(self):
        if self.verificare:
            self.modify_len -= 1
            self.tablou_len_data()
        elif self.verificare is False:
            self.incercari += 1
            self.tablou_scor()
