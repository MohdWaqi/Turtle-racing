from turtle import Turtle, Screen
import random

colour = ["red", "yellow", "green", "blue", "black", "brown"]


# def move_forward():
#     tom.forward(10)
#
#
# def move_backward():
#     tom.back(10)
#
#
# def move_left():
#     tom.left(10)
#
#
# def move_right():
#     tom.right(10)
#
#
# def clear():
#     tom.reset()
#
screen = Screen()
is_race_on = False
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear, "c")
screen.setup(width=500, height=400)
user = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour?: ")
all_turtles = []
for color in colour:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-100 + colour.index(color) * 50)
    all_turtles.append(new_turtle)
if user:
    is_race_on = True
while is_race_on:
    for object in all_turtles:
        if object.xcor() > 230:
            is_race_on = False
            winner = object.pencolor()
            if user == winner:
                print(f"You win! The {winner} turtle wins.")
            else:
                print(f"You lose! The {winner} turtle wins.")
        object.forward(random.randint(0,10))

screen.exitonclick()

