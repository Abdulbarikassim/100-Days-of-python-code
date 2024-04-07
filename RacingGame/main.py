from turtle import Turtle,Screen
from car_manager import CarManger
from player import Player
from scoreboard import Scoreboard
import time 


screen = Screen()
screen.setup(width=800,height=600)
screen.tracer(0)



car_manager = CarManger()




is_game_on = True

while is_game_on:
  screen.update()
  time.sleep(0.1)
  car_manager.create_car()
  car_manager.move()
  

























screen.exitonclick()
 