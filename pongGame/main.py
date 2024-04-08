from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


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
ball = Ball()
scoreboard = Scoreboard()



screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  ball.move()
  
  # Detect collision with wall and bounce 
  if  (ball.ycor() > 280 or 
       ball.ycor() <-280 ):
    # it needs to bounce. 
       ball.bounce_y()
       
  # Detect collision with the paddle and bounce.
  
  if ball.distance(r_paddle) < 40 or ball.distance(l_paddle) < 40  :
    ball.bounce_x()
    
  # Detect when the ball misses the paddle .
  # what should happen is: 
  #1. the ball should come back to the center and the ball moves in opposite direction.
  #2. According to  where the ball missed the opposite opponent get's a point.
  
  if ball.xcor() > 390  : 
    ball.reset_position()
    scoreboard.increase_lScore()

  if ball.xcor() < -390 : 
    ball.reset_position()
    scoreboard.increase_rScore()
    
        
  
  
  
  

















screen.exitonclick()
