from turtle import Turtle


# create a ball class.

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.shapesize(stretch_wid=1)
        