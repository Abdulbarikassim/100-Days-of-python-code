from turtle import Turtle


# create a ball class.

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.shapesize(stretch_wid=1)
    self.penup()
    self.x_move = 10    
    self.y_move = 10
    
  def move(self):
    new_y = self.ycor() + self.x_move
    new_x = self.xcor() + self.y_move
    self.goto(new_x,new_y)