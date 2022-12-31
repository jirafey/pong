import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
# Combo
combo = 0
# Paddle A
wid = 5.1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=wid, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=wid, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1 # higher speed, collision is not deteceted correctly
ball.dy = 0.1 # higher speed, collision is not deteceted correctly

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Pen_combo
pen_combo = turtle.Turtle()
pen_combo.speed(0)
pen_combo.shape("square")
pen_ball_color = ball.color()[0]
pen_combo.color("white")
pen_combo.penup()
pen_combo.hideturtle()
pen_combo.goto(0, 230)
pen_combo.write(combo, align="center", font=("Courier", 24, "bold"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def color_paddle_a():
    # Paddle_a colors left one
    if ball.color() == ('pink', 'pink'):
        ball.color('yellow')
    elif ball.color() == ('blue', 'blue'):
        ball.color('orange')
    elif ball.color() == ('green', 'green'):
        ball.color('red')
    elif ball.color() == ('gray', 'gray'):
        ball.color('lightgreen')
    elif ball.color() == ('magenta', 'magenta'):
        ball.color('cyan')
    elif ball.color() == ('purple', 'purple'):
        ball.color('yellow')
    elif ball.color() == ('white', 'white'):
        ball.color('yellow')
def color_paddle_b():
    if ball.color() == ('orange', 'orange'):
        ball.color('green')
    elif ball.color() == ('yellow', 'yellow'):
        ball.color('blue')
    elif ball.color() == ('white', 'white'):
        ball.color('pink')
    elif ball.color() == ('red', 'red'):
        ball.color('gray')
    elif ball.color() == ('lightgreen', 'lightgreen'):
        ball.color('magenta')
    elif ball.color() == ('cyan', 'cyan'):
        ball.color('purple')

# Making sure the paddles will not fly out of the visible screen (horizontal axis)
def flying_paddle():
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Combo
    pen_ball_color = ball.color()[0]
    pen_combo.color(pen_ball_color)
    pen_combo.clear()
    pen_combo.write("Combo: {}".format(combo), align="center", font=("Courier", 24, "normal"))

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking: Top and bottom
    if ball.ycor() > 288:
        ball.sety(288)
        ball.dy *= -1
        winsound.PlaySound('beep3.wav', winsound.SND_ASYNC)
    elif ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound('beep3.wav', winsound.SND_ASYNC)

    #Border checking: Left and right
    if ball.xcor() > 344:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        ball.color('white')
        combo = 0

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        ball.color('white')
        combo = 0

    # Paddle and ball collisions
    if ball.xcor() < -330 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        if ball.xcor() != -330.00000000000654:
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            ball.color('white')
            ball.dx *= -1
            combo = 0


        ball.dx *= -1
        winsound.PlaySound('beep3.wav', winsound.SND_ASYNC)
        color_paddle_a()
        combo += 1
    elif ball.xcor() > 330 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:

        if ball.xcor() !=  330.00000000000654:
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
            ball.color('white')
            ball.dx *= -1
            combo = 0
        ball.dx *= -1
        winsound.PlaySound('beep3.wav', winsound.SND_ASYNC)
        color_paddle_b()
        combo += 1

    # Making sure the paddles will not fly out of the visible screen (horizontal axis)
    flying_paddle()
    # make a smaller paddle after some time or make speed increase with delta time
    # collision with the paddle after it is behind the mark that gives a point ot player grants +1 combo