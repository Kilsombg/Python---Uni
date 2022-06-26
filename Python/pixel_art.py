import turtle

t = turtle.Turtle()
turtle.title("")
turtle.delay(0)
turtle.tracer(0,0)
turtle.setup(600,650)  # widht, height
side = 10

# move the turtle
t.penup()
t.goto(-210, -270)
t.pendown()

# set the turtle
t.width(1)
numSquares = 42

def drawSquare(color):
    t.color(color)
    t.ht()
    t.speed(0)
    t.begin_fill()
    for i in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill()
    t.forward(side)

def nextRow():
    t.penup()
    t.backward(numSquares * side)
    t.left(90)
    t.forward(side)
    t.right(90)
    t.pendown()
    turtle.update()

def drawRow(colors, numbers):
    for j in range(len(colors)):
        for k in range(numbers[j]):
            drawSquare(colors[j])
    nextRow()


"""
------------>  135
|
|
|
|
V

"""

# COLOR PALLETE
wh = "white"
bl = "black"
gr1 = "gray40"
gr2 = "gray20"


# DRAWING

# color code
colors = [
    [wh, bl, gr1, wh, gr1, bl, wh, gr1, bl, wh],
    [wh, gr2, bl, gr1, wh, gr1, bl, wh, gr1, bl, gr2, wh, gr1, bl, gr1, bl, wh],
]

# times per color
numbers = [
   [],
]

# looping through colors
for i in range(len(colors)):
    drawRow(colors[i], numbers[i])

t = input()