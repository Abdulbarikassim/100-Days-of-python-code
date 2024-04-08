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
    self.move_speed = 0.1
    
  def move(self):
    new_x = self.xcor() + self.x_move 
    new_y = self.ycor() + self.y_move
    self.goto(new_x,new_y)

  def bounce_y(self): # bounce the ball reverse  to the y-axis.
    self.y_move *= -1
  
  def bounce_x(self):  # bounce the ball reverse  to the x -axis.
    self.x_move *= -1 
    self.move_speed *= 0.9
  
  def reset_position(self):
    self.goto(0,0)
    self.move_speed = 0.1
    self.bounce_x()
    