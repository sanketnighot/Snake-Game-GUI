import turtle
import random
from time import sleep

# Setup the Screen

delay = 0.1
# Score
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game By @SanketNighot ")
colors = ["yellow", "green", "blue", "cyan", "pink", "orange", "teal", "lime"]
bgc = random.choice(colors)
wn.bgcolor(bgc)
wn.setup(width=700, height=700)
wn.tracer(0)  # Turns off the screen updates

# Creating Snake

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segment = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("brown")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Score: 0     High Score: 0", align="center", font=("Courier", 24, "normal"))


# Function :

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard Binding

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "W")
wn.onkeypress(go_down, "S")
wn.onkeypress(go_left, "A")
wn.onkeypress(go_right, "D")

# Main Game Loop
while True:
    wn.update()
    # Check For Collision
    if head.xcor() > 335 or head.xcor() < -335 or head.ycor() > 335 or head.ycor() < -335:
        sleep(2.0)
        head.goto(0, 0)
        head.direction = "stop"

        for seg in segment:
            seg.goto(1000, 1000)
        # Clear Segment list
        segment.clear()
        # Reset the Score and Delay
        delay = 0.1
        score = 0
        pen.clear()
        pen.write(f"Score: {score}     High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
        bgc = random.choice(colors)
        wn.bgcolor(bgc)

    # Check for Collision
    if head.distance(food) < 20:
        # Move the food to random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)

        # Add a Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

        delay -= 0.001

        # Increase the Score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}     High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move end segment first is

    for index in range(len(segment) - 1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)

    # Move Segment 0 where Head
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)

    move()
    for seg in segment:
        if seg.distance(head) < 20:
            sleep(2.0)
            head.goto(0, 0)
            head.direction = "stop"
            for seg in segment:
                seg.goto(1000, 1000)
            # Clear Segment list
            segment.clear()
            # Reset the Score and Delay
            delay = 0.1
            score = 0
            pen.clear()
            pen.write(f"Score: {score}     High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
            bgc = random.choice(colors)
            wn.bgcolor(bgc)

    sleep(delay)

wn.mainloop()
