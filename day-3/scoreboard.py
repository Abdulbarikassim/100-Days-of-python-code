from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0,270)
    self.hideturtle()
    self.write(f"Score: {self.score}",align="center",font=("courier",24,"normal"))
    
  def update(self):
    self.score+= 1
    self.clear()
    self.write(f"Score: {self.score}",align="center",font=("courier",24,"normal"))

    
    