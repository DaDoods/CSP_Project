from turtle import *

from block import Block


#TODO: remove block from list if they collide with the ball
class Ball(Turtle):
    def __init__(self, dx: int, dy: int, y_init: int): #Initialize the ball
        self.dx = dx
        self.dy = dy
        super().__init__(shape='circle')
        self.turtlesize(2)
        self.radius = 20
        self.color('white')
        self.pu()
        self.sety(y_init)
    def Xmove(self, xDist: int): #Move left of rigt
        self.setx(self.xcor()+xDist)
    def Ymove(self, yDist): #Move top or down
        self.sety(self.ycor()+yDist)
    def bounce(self, wnWidth: int, wnHeight: int): #Move the move and bounce if it hits a wall
        if self.xcor() + self.radius > wnWidth/2 or self.xcor() - self.radius < -wnWidth/2: # right and left collisions
            self.dx = -self.dx
        if self.ycor() + self.radius > wnHeight/2: # top collisions
            self.dy = -self.dy
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
    def out(self, ycor: int): #Check if the ball has gone bellow the paddle
        if self.ycor() + self.radius < ycor:
            return True
    def Coliide(self, block: Block): #Check collisions between block and ball
        self.xCollide = self.radius + block.length #Amount of distance to be considered as a collison
        self.yCollide = self.radius + block.height
        if abs(self.xcor()-block.xcor()) <= self.xCollide and abs(self.ycor() - block.ycor()) <= self.yCollide: #Check if there is a collisions
            #==========Check which side the ball collides with =========#
            if abs(self.ycor() - self.radius - block.topSide()) < self.yCollide and self.dy < 0: #check for top collisions
                self.dy *=-1
            if abs(self.ycor() + self.radius - block.bottonSide()) < self.yCollide and self.dy > 0: #check for bottom collisions
                self.dy *=-1
            if abs(self.xcor() + self.radius - block.leftSide()) < self.xCollide and self.dx > 0: #check for left collisions
                self.dx *=-1
            if abs(self.xcor() - self.radius - block.rightSide()) < self.xCollide and self.dx < 0: #check for right collisions
                self.dx *=-1
            return True