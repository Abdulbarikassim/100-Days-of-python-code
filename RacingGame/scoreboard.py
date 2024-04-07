from turtle import Turtle

FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-250,250)
        self.write(f"Score : {self.score}",font=FONT)
        
    
    def game_over(self):
      self.goto(0,0)
      self.write(f"GAME OVER!",font=FONT)

    
    def increase_score(self):
      self.clear()
      self.score += 1
      self.write(f"Score :{self.score}",font=FONT)

      