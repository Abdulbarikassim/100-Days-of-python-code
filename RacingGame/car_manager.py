from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManger():
  def __init__(self):
    self.cars = []
    
    
  def create_car(self):
    random_generate = random.randint(1,6)
    if random_generate == 1:
      new_car = Turtle("square")
      new_car.shapesize(stretch_len=2)
      new_car.color(random.choice(COLORS))
      new_car.penup()
      random_y = random.randint(-250,250)
      new_car.goto(360,random_y)
      self.cars.append(new_car)
      self.speed_up = STARTING_MOVE_DISTANCE
    
  def move(self):
    for cars in self.cars:
      cars.backward(self.speed_up)
    
    
  def level_up(self):
    self.speed_up += 10
    
    
    
      