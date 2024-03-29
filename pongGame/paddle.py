from turtle import Turtle



# create the paddle class.
class Paddle(Turtle):
  def __init__(self,position):
    super().__init__() # inherits the Turtles class.
    self.shape("square")
    self.color("white")
    self.penup()
    self.shapesize(stretch_wid=4,stretch_len=1)
    self.goto(position)
    self.x_move = 20
    self.y_move = 20
    
  
  # create move method.
  
  def go_up(self):
    new_y = self.ycor() + self.y_move
    self.goto(self.xcor(),new_y)
    
  def go_down(self):
     new_y = self.ycor() - self.y_move
     self.goto(self.xcor(),new_y)
   