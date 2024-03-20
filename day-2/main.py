from turtle import Turtle,Screen
import random 

turtles = []

is_game_on = False

screen = Screen()
screen.setup(height=500,width=500)
user_bet  = screen.textinput(title="Enter your bet.",prompt="Enter the color of the turtle that will win the race: ")
colors = ["red","brown","green","blue","yellow","purple"]

for i in range(0,6):
  new_turtle = Turtle("turtle")
  new_turtle.color(colors[i])
  new_turtle.penup()
  new_turtle.goto(x=-230,y=-100+i*40)
  turtles.append(new_turtle)
  

# if user_bet:
#   is_game_on = True
  
# while is_game_on:
#   for turtle in turtles:
#     if turtle.xcor() > 230:
#       is_game_on = False
#       winning_color = turtle.pencolor()
#       if winning_color == user_bet:
      
#         print(f"You've WON! {winning_color} is the color of the winning Turtle.")
#       else:
#         print(f"You've LOST! {winning_color} is the color of the winning Turtle.")

#     rand_distance = random.randint(0,10)
#     turtle.forward(rand_distance)
















screen.exitonclick()
