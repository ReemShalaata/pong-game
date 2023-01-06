from turtle import Turtle
MAX_POSITION=300
MIN_POSITION=-300
STEP=30
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.speed("fast")
        self.penup()

    def up(self):
        self.goto(self.xcor(),self.ycor()+STEP)

    def down(self):
        self.goto(self.xcor(),self.ycor()-STEP)

