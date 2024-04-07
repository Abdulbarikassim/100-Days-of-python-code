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
scoreboard = Scoreboard()


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
      scoreboard.game_over()
      
  #check if the player reaches at the top of the screen.
  
  if player.at_finish_line():
    player.reset_position()
    scoreboard.increase_score()
    
  
      
      

























screen.exitonclick()
 