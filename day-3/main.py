from turtle import Turtle,Screen
from snake import Snake 
import time
from food import Food 
from scoreboard import Scoreboard
turtle = Turtle()
screen = Screen()



snake = Snake()
food = Food()
scoreboard= Scoreboard()

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
  # Detect collision with the food.
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.update()
    
    
    
  # detect collision with the wall.
  
  if (snake.head.xcor() > 290 or 
      snake.head.xcor() < -290 or 
      snake.head.ycor() > 290 or 
      snake.head.ycor() < -290):
      scoreboard.game_over()
      game_is_on = False 
      
    
    
  











screen.exitonclick()
