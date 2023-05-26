from turtle import *

from ball import Ball
from random import randint


class Paddle(Turtle):
    def __init__(self, y_init:int): #Initialize the Paddle
        self.length = 120
        self.height = 10
        self.move = 5
        super().__init__(shape='square')
        self.pu()
        self.shapesize(stretch_len=self.length/10, stretch_wid=self.height/10)
        self.color('orange')
        self.sety(y_init)
    def topSide(self): #Give the top side cord
        return self.ycor() + self.height
    def rightSide(self): #Give the right side cord
        return self.xcor() + self.length
    def leftSide(self): #Give the left side cord
        return self.xcor() - self.length
    def bottomSide(self): #Give the bottom side cord
        return self.ycor() - self.height
    def Collide(self, ball: Ball): #Check for collisions between paddle and ball
        self.xCollide = ball.radius + self.length #Amount of distance to be considered as a collison
        self.yCollide = ball.radius + self.height
        if abs(ball.xcor() - self.xcor()) <= self.xCollide and abs(ball.ycor() - self.ycor()) <= self.yCollide:
            if abs(ball.ycor() - ball.radius - self.topSide()) < self.yCollide and ball.dy < 0: #Top collisions with paddle
                ball.dy *=-1
                #=========Check for where the collisions happens==========#
                if ball.dx > 0:
                    if self.leftSide() <= ball.xcor() < self.xcor():
                        ball.dx = randint(3,5)
                else:
                    if self.xcor() <= ball.xcor() <= self.rightSide():
                        ball.dx = randint(-5,-3)
            if abs(ball.xcor() - ball.radius - self.rightSide()) < self.xCollide and ball.dx < 0: #Right side Collisions
                ball.dx *=-1
            if abs(ball.xcor() + ball.radius - self.leftSide()) < self.xCollide and ball.dx > 0: #Left side Collisions
                ball.dx *=-1
    