from turtle import Turtle,Screen
import random

s = Screen()
s.setup(width=500, height=400)
is_race_on = False
user_bet = s.textinput(title="Make A Bet.", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for j in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[j])
    new_turtle.goto(x=-230,y=-100 + j*35)
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

s.exitonclick()