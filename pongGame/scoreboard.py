from turtle import Turtle

class Scoreboard(Turtle):# inherits the Turtle module.
  def __init__(self):
    super().__init__()
    self.r_score = 0
    self.l_score = 0
    self.color("white")
    self.penup()
    self.hideturtle()
    self.update_score()
    
  def update_score(self):
    self.clear()
    self.goto(100,200)
    self.write(f"{self.r_score}",font=("courier",60,"normal"))
    self.goto(-100,200)
    self.write(f"{self.l_score}",font=("courier",60,"normal"))
    
  def increase_rScore(self):
    self.r_score += 1
    self.update_score()

  def increase_lScore(self):
    self.l_score += 1
    self.update_score()
        