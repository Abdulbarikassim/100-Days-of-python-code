from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
      self.forward(10)
      
    
    def at_finish_line(self):
      if Player.ycor() > 280:
        return True
      else:
        return False
    
    def reset_position(self):
      self.goto(STARTING_POSITION)
      
      