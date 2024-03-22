from turtle import Turtle, Screen


screen = Screen()
turtle = Turtle()

screen.listen()


STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT  = 180
RIGHT = 0


class Snake():
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head =self.segments[0]
    
  def create_snake(self):
    for position in STARTING_POSITIONS:
      new_turtle = Turtle("square")
      new_turtle.color("white")
      new_turtle.penup()
      new_turtle.goto(position)
      self.segments.append(new_turtle)
      
  def move(self):
      for seg_num in range(len(self.segments)-1,0,-1):
        x= self.segments[seg_num-1].xcor()
        y= self.segments[seg_num-1].ycor()
        self.segments[seg_num].goto(x,y)
        
      self.head.forward(MOVE_DISTANCE)
      
  def go_up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
  
  
  def go_down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
  
  def go_left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
  def go_right(self):  
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
    