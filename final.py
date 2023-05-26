from random import choice
from turtle import *

import game
from ball import Ball
from paddle import Paddle

#==========SetUp==========#
wn = Screen()
wnWidth, wnHeight = 1280, 720
speed = dx, dy = choice([-3, 3]) , 3#Ball movement 
ball_init = -200
wn.setup(wnWidth, wnHeight)
wn.bgcolor('black')
wn.listen()
intro = True
running = True
img = "pictures\\finaldarock.gif"
win = "pictures\\winScreen.gif"
wn.addshape(img)
wn.addshape(win)
wn.tracer(False)

#==========Functions==========#
def quit(): #close window while game is running
    global running
    running = False

def exitGame(): #exit game when game is over
    global gameOver, running
    gameOver = False
    running = False

def starts(*args):
    global intro
    intro = False

def GG(): #End screen
    wn.clearscreen()
    wn.bgcolor('black')
    wn.tracer(False)
    gg = Turtle()
    gg.ht()
    gg.pu()
    gg.pencolor('red')
    gg.write('Game Over', align='center', font=('Arial', 72, 'bold'))
    gg.sety(-100)
    gg.write("Press ESCAPE to quit", align='center', font=('Arial', 36, 'bold'))
    wn.tracer(True)

def move(event):
    x = event.x - wnWidth/2
    if running:
        paddle.setx(x)
        #==========Wall Collisions==========#
        if paddle.xcor() - paddle.length < -wnWidth/2:
            paddle.setx(-wnWidth/2 + paddle.length)
        if paddle.xcor() + paddle.length > wnWidth/2:
            paddle.setx(wnWidth/2- paddle.length)

#==========Intructions========#
start = Turtle()
start.ht()
start.pencolor("red")
start.write('Click Screen to Start', align='center', font=("Arial", 48, "bold"))
while intro:
    wn.onclick(starts)
    wn.update()

start.clear()
intro = Turtle()
intro.pu()
intro.ht()
intro.goto(350, -250)
intro.pencolor('red')
intro.write('Use your mouse\n to move the paddle', align='center', font=('Arial', 24, 'bold')) 

#==========Creating Objects==========#
ball = Ball(dx,dy, ball_init)
paddle = Paddle(ball_init-ball.radius-10)
rows = game.grid(wn)
game.csp(rows)
game.darcok(wn, img, rows)
wn.tracer(True)
wn.tracer(0)

#==========Game==========#
while running:
    gameOver = ball.out(-wnHeight/2) #Check if ball has fallen below paddle
    if gameOver:
        GG()
        while gameOver:
            onkey(exitGame, 'Escape') #Restart game or quit game
            wn.update()
    for row in rows: #Check Collisons between ball and blocks
        for block in row:
            collision = ball.Coliide(block)
            if collision:
                row.remove(block)
                block.hideturtle()
    if not(any(rows)):
        wn.clearscreen()
        wn.bgpic(win)
    paddle.Collide(ball) #Check Collisons between ball and paddle
    ball.bounce(wnWidth, wnHeight) #Bounce the ball
    #==========Inputs==========#
    getcanvas().bind('<Motion>', move)
    onkey(quit, "Escape")
    wn.update()