from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500, height=400)

colors=["red", "yellow", "blue", "green", "purple", "orange"]
turtles=["tim", "jim", "zazu", "miti", "dorin", "oaie"]
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will winn the race? Pick a color")

start_height=150
color_number=0

power_turtles=[]

for name in turtles:
    name = Turtle(shape="turtle")
    name.color(colors[color_number])
    color_number+=1
    name.penup()
    name.goto(x=-230, y=start_height)
    start_height -= 60
    power_turtles.append(name)

print(power_turtles)


if user_bet:
    turtle_race=True

while turtle_race:
    for turtle in power_turtles:
        if turtle.xcor()>230:
            turtle_race=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print("winner")
            else:
                print(f"loser. the winner is {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
