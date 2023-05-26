from turtle import *


class Block(Turtle):
    def __init__(self, wn: Screen): #Initialize the blocks
        self.length = 60
        self.height = 30
        super().__init__(shape='square')
        self.pu()
        self.shapesize(stretch_len=self.length/10, stretch_wid=self.height/10)
        self.color('white')
    def leftSide(self): #Give the left side cord
        return self.xcor()-self.length
    def rightSide(self): #Give the right side cord
        return self.xcor()+self.length
    def topSide(self): #Give the top side cord
        return self.ycor()+self.height
    def bottonSide(self): #Give the bottom side cord
        return self.ycor()-self.height