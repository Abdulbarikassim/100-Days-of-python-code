from turtle import Turtle,Screen
from paddle import Paddle
turtle = Turtle()
screen  =Screen()

# create the screen.
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME.")
screen.tracer(0)
# create paddle objects.

r_paddle = Paddle((350,0)) # right paddle.
l_paddle = Paddle((-350,0)) # left paddle.

screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"W")
screen.onkey(l_paddle.go_down,"S")



game_is_on = True

while game_is_on:
  screen.update()
  
  
  

















screen.exitonclick()
