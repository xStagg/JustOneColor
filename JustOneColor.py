from tkinter import *
from random import *
import json

tk = Tk()
tk.title("Just One Color")

cv = Canvas(tk, width=430, height=370)
cv.pack()


NE = PhotoImage(file="2NE.png").subsample(14)  # 2
NS = PhotoImage(file="2NS.png").subsample(14)  # 4
NW = PhotoImage(file="2NW.png").subsample(14)  # 6
SE = PhotoImage(file="2SE.png").subsample(14)  # 8
SW = PhotoImage(file="2SW.png").subsample(14)  # 10
WE = PhotoImage(file="2WE.png").subsample(14)  # 12
NSWE = PhotoImage(file="4arrows.png").subsample(14)  # 14
NONE = PhotoImage(file="NONE.png").subsample(14)  # 16
arrowtypes = [NE, NS, NW, SE, SW, WE, NSWE, NONE]
arrowtypesstr = ["NE", "NS", "NW", "SE", "SW", "WE", "NSWE", "None"]

with open('config.json') as f:
    config = json.load(f)

arrows = []
squares = []
row = 0
n = 0
for j in range(3):
    row += 1
    col = 0
    for i in range(4):
        n += 1
        col += 1

        x1 = 100+60*i
        y1 = 100+60*j
        x2 = x1+50
        y2 = y1+50

        square = cv.create_rectangle(
            x1, y1, x2, y2, fill=config[str(n)]["color"])

        arrowtype = arrowtypes[arrowtypesstr.index(
            config[str(n)]["arrow"])]
        arrow = cv.create_image(
            x1+25, y1+25, image=arrowtype, tag=(str(arrowtype), row, col))

        squares.append(square)
        arrows.append(arrow)


def Clicked(event):
    arrow = cv.find_closest(event.x, event.y)[0]
    item = cv.find_closest(event.x, event.y)[0]-1

    row = int(cv.itemcget(arrow, 'tag')[9:11])
    col = int(cv.itemcget(arrow, 'tag')[11:13])

    arrowtypec = cv.itemcget(arrow, 'tag')[:9]

    items = [item]
    if arrowtypec == "pyimage2 ":
        print("NE")
        if row > 1:
            items.append(item-8)
        if col < 4:
            items.append(item+2)
    elif arrowtypec == "pyimage4 ":
        print("NS")
        if row > 1:
            items.append(item-8)
        if row < 3:
            items.append(item+8)
    elif arrowtypec == "pyimage6 ":
        print("NW")
        if row > 1:
            items.append(item-8)
        if col > 1:
            items.append(item-2)
    elif arrowtypec == "pyimage8 ":
        print("SE")
        if row < 3:
            items.append(item+8)
        if col < 4:
            items.append(item+2)
    elif arrowtypec == "pyimage10":
        print("SW")
        if row < 3:
            items.append(item+8)
        if col > 1:
            items.append(item-2)
    elif arrowtypec == "pyimage12":
        print("WE")
        if col > 1:
            items.append(item-2)
        if col < 4:
            items.append(item+2)
    elif arrowtypec == "pyimage14":
        print("NSWE")
        if row > 1:
            items.append(item-8)
        if row < 3:
            items.append(item+8)
        if col > 1:
            items.append(item-2)
        if col < 4:
            items.append(item+2)

    for item in items:
        current_color = cv.itemcget(item, 'fill')

        if current_color == 'red':
            cv.itemconfig(item, fill='green')
        else:
            cv.itemconfig(item, fill='red')

    finish = False
    for i in range(len(squares)-1):
        if cv.itemcget(squares[i], 'fill') == cv.itemcget(squares[i+1], 'fill'):
            finish = True
        else:
            finish = False
            return
    if finish == True:
        print("Vous avez gagné !")


cv.bind('<Button-1>', Clicked)

tk.mainloop()
