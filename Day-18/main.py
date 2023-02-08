from turtle import Turtle, Screen
import heroes, random

timmy = Turtle()

timmy.shape("turtle")
timmy.shapesize(2,2,2)
timmy.color("green")

### Square
# for i in range(0,4):
#     timmy.forward(100)
#     timmy.left(90)

### dash line
# for i in range(20):
#     timmy.pendown()
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)

### draw different shapes
# count = 3
# while count<11:
#     for i in range(count):
#         timmy.forward(100)
#         timmy.right(360/count)
#     count+=1

### draw different shapes II

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
# for shape_side_n in range (3,11):
#     draw_shape(shape_side_n)

### random walk
colors = ["red", "blue", "green", "yellow", "brown"]
color = random.choice(colors)
angle = [0,90,180,270]
choice_binary = ["0", "1"]
print(color)
print(random.choice(angle))
timmy.pensize(15)
timmy.speed(10)
for i in range(50):
    timmy.forward(20)
    timmy.pencolor(random.choice(colors))
    if random.choice(choice_binary) == "0":
        timmy.right(random.choice(angle))    
    else:
        timmy.left(random.choice(angle))

screen = Screen()
screen.exitonclick()
print(heroes.gen())