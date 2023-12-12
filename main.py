from turtle import Screen, Turtle
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create snake body
segments = []
positions = [(0, 0), (-20, 0), (-40, 0)]

for seg in range(3):
    global snake_seg
    snake_seg = Turtle()
    snake_seg.penup()
    snake_seg.color("orange")
    snake_seg.shape("square")
    snake_seg.goto(positions[seg])
    segments.append(snake_seg)

snake_head = segments[0]


# move the snake
def move_up():
    if snake_head.heading() != 270:
        snake_head.setheading(90)


def move_down():
    if snake_head.heading() != 90:
        snake_head.setheading(270)


def move_left():
    if snake_head.heading() != 0:
        snake_head.setheading(180)


def move_right():
    if snake_head.heading() != 180:
        snake_head.setheading(0)


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(move_down, "Down")

# draw food
food = Turtle()
food.shape("square")
food.color("red")
food.penup()


# distribute food randomly
def place_food():
    x_rand = random.randint(-280, 280)
    y_rand = random.randint(-280, 280)
    food.goto(x_rand, y_rand)


place_food()


def add_segment():
    new_seg = Turtle()
    new_seg.color("orange")
    new_seg.shape("square")
    new_seg.penup()
    new_seg.goto(segments[len(segments) - 1].xcor(), segments[len(segments) - 1].ycor())
    segments.append(new_seg)


# Game loop

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # make the snake parts follow each other when turning
    for seg_num in range(len(segments) - 1, 0, -1):
        new_xcor = segments[seg_num - 1].xcor()
        new_ycor = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_xcor, new_ycor)
    snake_head.forward(20)

    # detect collision with food
    if snake_head.distance(food) < 20:
        add_segment()
        place_food()

    # detect collision with wall
    if snake_head.xcor() > 288 or snake_head.xcor() < - 288 or snake_head.ycor() > 288 or snake_head.ycor() < - 288:
        game_on = False

    # detect collision with self
    for segment in segments:
        if snake_head.distance(segment) < 10:
            if segment == segments[0]: continue
            game_on = False
"test"
"test"
"another test"
screen.exitonclick()
