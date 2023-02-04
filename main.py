import turtle
screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Joc interactiv cu enumerarea tuturor judetelor din Romania')
screen.setup(width=1050, height=1000)
imagine = 'Romania_counties_blank_big.gif'
screen.addshape(imagine)
turtle.shape(imagine)


def click_map(x, y):
    global coordonat
    coordonat = x, y
    print(coordonat)
    print(type(coordonat))



screen.onscreenclick(click_map)



screen.mainloop()