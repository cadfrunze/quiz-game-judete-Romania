import turtle
import pandas as pd
import random
from tkinter import messagebox
import time
import sys

COLORS = ['red', 'green', 'blue', 'brown', 'purple', 'black']
dt = pd.read_csv('./files_for_game/map_Romania.csv')

dimension = 10


class Robotzelu:
    """
    Creearea schemei a jocului, include:

        1. Fereastra-box pt a raspunde,

        2. Verificare raspuns,

        3. Afisare nume judet daca raspunsul este corect, pe desen conform coordonatelor
    """

    def __init__(self):
        self.obiect = turtle.Turtle()
        self.ecran = turtle.Screen()
        self.obiect.penup()
        self.obiect.hideturtle()
        self.ver_raspuns = []
        self.check = None

    def raspunde(self):
        self.raspuns = self.ecran.textinput(title='Scrie un judet din Ro', prompt='Raspunde aici').title()
        self.verificare_raspuns()

    def verificare_raspuns(self):
        self.verificare_cuvant()
        while self.raspuns in self.ver_raspuns:
            messagebox.showinfo(title=f'{self.raspuns}', message='Ai mai scris acest judet')
            self.raspuns = self.ecran.textinput(title='Scrie un judet din Ro', prompt='Raspunde aici').title()
        else:
            if self.raspuns == 'Exit':
                ver_elem = dt.judet.to_list()
                new_list = [elem for elem in ver_elem if elem not in self.ver_raspuns]
                data_dict = {}
                data_dict['judet'] = new_list
                new_data = pd.DataFrame(data_dict)
                new_data.to_csv('./files_for_game/judete_care_trebuie_invatate.csv')
                sys.exit()
            if self.raspuns in dt.judet.to_list():
                afirmatie = dt[dt.judet == self.raspuns]
                coor = (int(afirmatie.x), int(afirmatie.y))
                messagebox.showinfo(title='Validat!', message='Raspuns corect!')
                raspuns_corect = afirmatie.judet.to_list()
                time.sleep(1)
                self.obiect.color(random.choice(COLORS))
                self.obiect.goto(coor)
                self.obiect.write(arg=f'{raspuns_corect[0]}', font=('Arial', dimension, 'normal'))
                self.ver_raspuns.append(raspuns_corect[0])
                self.check = True

            else:
                messagebox.showerror(title='Gresit!', message='Raspuns incorect!')
                self.check = False
            return self.check

    def verificare_cuvant(self):
        if ' - ' in self.raspuns:
            self.raspuns = self.raspuns.replace(' - ', '-')
        elif ' -' in self.raspuns:
            self.raspuns = self.raspuns.replace(' -', '-')
        elif '- ' in self.raspuns:
            self.raspuns = self.raspuns.replace('- ', '-')
        elif ' ' in self.raspuns:
            self.raspuns = self.raspuns.replace(' ', '-')
