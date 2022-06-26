import turtle

t = turtle.Turtle()
turtle.title("A Rose For You!")
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
------------>  42
|
|
|
|
V
59

8.5 by each side
"""

# COLOR PALLETE
gr1 = "chartreuse" # bright
gr2 = "chartreuse4" # normal
gr3 = "DarkGreen" # dark

bl = "black"
wh = "white"

r1 = "coral"
r2 = "coral2"
r3 = "firebrick1"
r4 = "brown4"


# DRAWING

# color code
colors = [
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, gr3, bl, wh],
    [wh, bl, wh, bl, gr3, bl, wh],
    [wh, bl, gr1, bl, wh, bl, gr3, bl, gr3, bl, wh],
    [wh, bl, gr1, gr2, bl, wh, bl, gr3, bl, wh],
    [wh, bl, gr1, gr2, bl, wh, bl, gr3, bl, wh],
    [wh, bl, gr2, bl, gr1, bl, wh, bl, gr3, bl, wh],
    [wh, bl, wh, bl, gr2, bl, gr1, bl, wh, bl, gr3, bl, wh],
    [wh, bl, gr1, bl, gr2, bl, gr1, gr2, bl, wh, bl, gr3, bl, wh],
    [wh, bl, gr1, gr2, bl, gr1, gr2, bl, wh, bl, gr3, bl, wh],
    [wh, bl, gr2, bl, gr1, gr2, bl, wh, bl, gr3, bl, wh],
    [wh, bl, gr2, gr1, bl, wh, bl, gr3, bl, wh],
    [wh, bl, gr2, gr1, bl, wh, bl, gr3, bl, wh],
    [wh, bl, wh, bl, wh, bl, gr3, bl, wh],
    [wh, bl, wh, bl, wh, bl, r3, bl, gr3, bl, wh],
    [wh, bl, r3, bl, wh, bl, r2, r3, bl, wh],
    [wh, bl, r3, bl, r1, r2, r3, bl, wh],
    [wh, bl, r1, r2, r3, bl, wh],
    [wh, bl, r1, r4, bl, r2, r3, bl, wh],
    [wh, bl, r4, bl, r4, r1, r2, r3, bl, wh],
    [wh, bl, r3, r1, bl, r4, bl, r4, r1, r2, r3, bl, wh],
    [wh, bl, r3, r1, r4, bl, r2, r4, bl, r4, r1, r2, r3, bl, wh],
    [wh, bl, r3, r1, r4, bl, r2, r4, bl, r4, r1, r2, r3, bl, wh, bl, wh],
    [wh, bl, r3, r2, r1, r4, bl, r3, bl, r2, r4, bl, r1, r3, bl, r3, bl, wh],
    [wh, bl, r3, r2, r1, r4, bl, r3, bl, r2, r3, bl, r1, r2, r4, bl, r1, bl, r1, r2, r3, bl, wh],
    [wh, bl, r3, r2, r1, r4, bl, r3, bl, r4, r2, r3, bl, r1, r2, r4, bl, r1, r2, bl, r1, r2, r3, bl, wh],
    [wh, bl, r3, r2, r1, r4, bl, r3, r4, bl, r4, r1, r3, bl, r1, r2, r4, bl, r1, r2, bl, r1, r2, r3, bl, wh],
    [wh, bl, r3, r2, r1, bl, r3, r2, r3, r4, bl, r4, bl, r4, r1, r3, bl, r2, r4, bl, r1, r2, bl, wh],
    [wh, bl, r3, r2, r1, bl, r3, r2, r4, bl, r4, bl, r4, r1, r3, bl, r1, r4, bl, r1, r2, r3, bl, wh],
    [wh, bl, r3, r2, r1, bl, r3, r2, r1, bl, r3, r4, bl, r4, r1, r3, bl, r1, r4, bl, r1, r2, r3, bl, wh],
    [wh, bl, r3, r1, bl, r3, r2, r1, bl, r3, r1, bl, r3, r4, bl, r4, r1, r3, bl, r4, bl, r1, r2, r3, bl, wh],
    [wh, bl, r3, r1, bl, r3, r1, bl, r3, r2, r1, bl, r3, r1, r4, bl, r3, r2, r3, r4, bl, r4, bl, r4, r1, r3, bl, r2, bl, r1, r2, r3, bl, wh],
    [wh, bl, wh, bl, r3, r1, bl, r3, r2, r1, bl, r3, r1, r4, bl, r3, r2, r1, r2, r3, bl, r4, bl, r1, r2, r3, bl, r1, r2, bl, wh],
    [wh, bl, wh, bl, r3, bl, r3, r2, r1, bl, r4, bl, r2, r1, r2, bl, r4, r3, r2, r1, r2, r3, bl, r1, bl, wh],
    [wh, bl, r3, r2, r1, bl, r3, r4, bl, r1, r4, bl, r3, r2, r1, r2, r3, bl, r1, bl, wh],
    [wh, bl, r3, r2, r1, bl, r3, bl, r4, r3, bl, r4, bl, r4, r3, bl, r2, r1, r2, r3, bl, r1, bl, wh],
    [wh, bl, r3, r2, r1, bl, r4, r3, bl, r4, bl, r4, bl, r4, r1, r3, bl, r1, r2, r3, bl, r1, bl, wh],
    [wh, bl, r3, r2, r1, bl, r4, bl, r3, bl, r4, bl, r4, bl, r4, r1, r3, bl, r1, r2, r3, bl, r1, bl, wh],
    [wh, bl, r3, r2, r1, bl, r4, bl, r4, bl, r3, r4, bl, r1, r3, bl, r2, r3, bl, r1, bl, wh],
    [wh, bl, r3, r2, r1, bl, r4, bl, r3, bl, r1, bl, r2, r3, bl, r1, bl, wh],
    [wh, bl, r3, r2, r1, r2, bl, r1, r2, r3, bl, wh, bl, wh],
    [wh, bl, r3, r2, bl, wh, bl, r2, r3, bl, wh],
    [wh, bl, r3, bl, wh, bl, r3, bl, wh],
    [wh, bl, wh, bl, wh],
]

# times per color
numbers = [
    [25, 1, 1, 1, 14],
    [25, 1, 1, 1, 14],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [26, 1, 1, 1, 13],
    [25, 2, 1, 1, 13],
    [24, 2, 2, 1, 13],
    [16, 4, 3, 1, 3, 1, 14],
    [15, 1, 4, 1, 1, 1, 1, 2, 1, 1, 14],
    [14, 1, 1, 5, 3, 1, 1, 1, 1, 14],
    [13, 1, 1, 6, 2, 1, 1, 2, 1, 14],
    [13, 1, 6, 1, 1, 1, 1, 1, 1, 1, 15],
    [10, 1, 1, 1, 4, 3, 2, 1, 1, 1, 1, 1, 15],
    [9, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 15],
    [8, 1, 1, 3, 1, 5, 2, 1, 2, 1, 1, 1, 15],
    [8, 1, 2, 2, 3, 3, 2, 2, 1, 2, 1, 15],
    [7, 1, 1, 5, 5, 4, 1, 1, 1, 16],
    [6, 1, 1, 1, 5, 8, 1, 2, 1, 16],
    [5, 4, 6, 5, 2, 1, 1, 1, 17],
    [5, 1, 4, 1, 3, 1, 5, 2, 1, 1, 18],
    [9, 1, 1, 1, 1, 1, 5, 2, 6, 15],
    [9, 1, 2, 1, 7, 2, 5, 1, 14],
    [10, 1, 14, 2, 1, 2, 12],
    [11, 1, 2, 6, 7, 1, 2, 1, 11],
    [12, 1, 1, 7, 2, 1, 1, 2, 4, 11],
    [12, 2, 3, 1, 1, 2, 2, 2, 1, 2, 3, 1, 10],
    [8, 4, 1, 1, 3, 1, 3, 2, 2, 1, 2, 2, 1, 1, 10],
    [5, 3, 4, 1, 1, 6, 3, 2, 1, 2, 2, 1, 1, 1, 3, 3, 3],
    [4, 1, 3, 3, 2, 1, 1, 5, 2, 3, 1, 4, 2, 1, 3, 3, 1, 2],
    [3, 1, 2, 2, 4, 1, 1, 1, 1, 3, 3, 1, 1, 2, 2, 1, 1, 2, 4, 2, 1, 1, 2],
    [3, 1, 1, 1, 5, 1, 1, 3, 1, 1, 3, 2, 1, 1, 3, 1, 1, 1, 1, 1, 4, 2, 1, 1, 1],
    [2, 1, 2, 1, 4, 1, 1, 3, 1, 2, 1, 4, 1, 1, 3, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1],
    [2, 1, 1, 1, 4, 2, 2, 1, 1, 1, 1, 1, 1, 3, 2, 1, 3, 1, 1, 1, 2, 1, 6, 2],
    [1, 1, 2, 1, 3, 1, 4, 1, 2, 1, 2, 3, 2, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 4],
    [1, 1, 1, 1, 4, 1, 2, 2, 1, 3, 1, 4, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2],
    [1, 1, 1, 2, 4, 2, 1, 1, 1, 1, 1, 1, 4, 2, 3, 2, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1],
    [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 1],
    [2, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 7, 1, 2, 1, 1, 1, 2, 1, 1, 1, 3, 1, 3],
    [7, 2, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 3],
    [8, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 4],
    [7, 1, 1, 2, 2, 2, 1, 1, 1, 1, 5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 4],
    [7, 1, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 4],
    [6, 4, 2, 1, 1, 3, 2, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 2, 1, 2, 1, 4],
    [10, 2, 1, 1, 3, 1, 2, 4, 1, 1, 1, 3, 1, 2, 3, 1, 1, 4],
    [12, 1, 1, 3, 6, 1, 3, 2, 1, 2, 1, 3, 2, 4],
    [12, 1, 4, 6, 1, 3, 1, 1, 1, 2, 10],
    [13, 4, 4, 2, 4, 1, 1, 1, 12],
    [17, 4, 7, 1, 13],
]

# looping through colors
for i in range(len(colors)):
    drawRow(colors[i], numbers[i])
    
t = input()