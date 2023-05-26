from turtle import *

from block import Block


def grid(wn: Screen):
    rows = []
    columns = []
    x = -565
    y = 300
    for row in range (5):
        for column in range (10):
            block = Block(wn)
            block.goto(x,y)
            columns.append(block) 
            x = x + 125
        rows.append(columns)
        columns = []
        x = -565
        y = y - 75
    return rows
#printing out CSP
def csp(rows):
    #C
    rows[0][0].color("red")
    rows[0][1].color("red")
    rows[0][2].color("red")
    rows[1][0].color("red")
    rows[2][0].color("red")
    rows[3][0].color("red")
    rows[4][0].color("red")
    rows[4][1].color("red")
    rows[4][2].color("red")
    #S
    rows[0][3].color("green")
    rows[0][4].color("green")
    rows[0][5].color("green")
    rows[0][6].color("green")
    rows[1][3].color("green")
    rows[2][3].color("green")
    rows[2][4].color("green")
    rows[2][5].color("green")
    rows[2][6].color("green")
    rows[3][6].color("green")
    rows[4][3].color("green")
    rows[4][4].color("green")
    rows[4][5].color("green")
    rows[4][6].color("green")
    #P
    rows[0][9].color("blue")
    rows[0][8].color("blue")
    rows[0][7].color("blue")
    rows[1][7].color("blue")
    rows[2][7].color("blue")
    rows[3][7].color("blue")
    rows[4][7].color("blue")
    rows[1][9].color("blue")
    rows[2][9].color("blue")
    rows[2][8].color("blue")
    
#darock
def darcok(wn: Screen, img: str, rows: list):
    for row in rows:
        for column in row:
            if column.color() == ('white', 'white'):
                column.shape(img)