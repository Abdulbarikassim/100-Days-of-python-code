from turtle import Turtle,Screen
from car_manager import CarManger
from player import Player
from scoreboard import Scoreboard
import time 


screen = Screen()
screen.setup(width=800,height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManger()
player = Player()

screen.onkey(player.go_up,"Up")



is_game_on = True

while is_game_on:
  screen.update()
  time.sleep(0.1)
  car_manager.create_car()
  car_manager.move()
  
  # check collision of player with cars.
  
  for cars in car_manager.cars:
    if cars.distance(player) < 20 :
      is_game_on = False
      
      

























screen.exitonclick()
 