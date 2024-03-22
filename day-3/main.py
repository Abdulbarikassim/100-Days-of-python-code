from turtle import Turtle,Screen
from snake import Snake 
import time

turtle = Turtle()
screen = Screen()



snake = Snake()

screen.bgcolor("black")
screen.title("SNAKE GAME.")
screen.setup(height=600,width=600)
screen.tracer(0)

screen.listen()

screen.onkey(snake.go_up,"Up")
screen.onkey(snake.go_down,"Down")
screen.onkey(snake.go_left,"Left")
screen.onkey(snake.go_right,"Right")

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  











screen.exitonclick()
