import turtle

# Init
win = turtle.Screen()
win.title('Pong by @Quantum')

win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

# Score
aScore = 0
bScore = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0 | Player B: 0", align='center', font=('Arial', 24, 'normal'))

# Paddle Movement
def paddle_a_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddle_a_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)
    
def paddle_b_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddle_b_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

# Main Game Loop
while True:
    win.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checks
    if ball.ycor() > 299:
        ball.sety(299)
        ball.dy *= -1 

    if ball.ycor() < -299:
        ball.sety(-299)
        ball.dy *= -1 

    if ball.xcor() > 399:
        ball.goto(0, 0)
        aScore += 1
        pen.clear()
        pen.write(f"Player A: {aScore} | Player B: {bScore}", align='center', font=('Arial', 24, 'normal'))
    if ball.xcor() < -399:
        ball.goto(0, 0)
        bScore += 1
        pen.clear()
        pen.write(f"Player A: {aScore} | Player B: {bScore}", align='center', font=('Arial', 24, 'normal'))
    
    # Paddle Collisions
    if (ball.xcor() > 349 and ball.xcor() < 370) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40):
        ball.setx(349)
        ball.dx *= -1
    if (ball.xcor() < -349 and ball.xcor() > -370) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40):
        ball.setx(-349)
        ball.dx *= -1
    
        
        

    