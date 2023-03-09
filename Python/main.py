import turtle

screen = turtle.Screen()
screen.setup(700,900)

t = turtle.Turtle()

turtle.delay(0)
turtle.tracer(0,0)
side = 8

# move the turtle
t.penup()
t.goto(-210, -100)
t.pendown()

# set the turtle
t.width(1)
numSquares = 58

def drawSquare(color):
    t.color(color)
    t.ht()
    t.speed(1)
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


# COLOR PALLETE
gr1 = "LimeGreen" # bright
gr2 = "ForestGreen" # normal
gr3 = "DarkGreen" # dark

bl1 = "PaleTurquoise" # bright
bl2 = "DarkCyan" # normal
bl3 = "MediumBlue" # dark

bl = "black"
wh = "white"

sk1 = (232,143,124) #"burlywood1"  # bright
sk2 = (200,84,59)  #"chocolate2"  # normal
sk3 = (137,45,25)  #"chocolate4"  # dark

y1 = "gold" # bright
y2 = "goldenrod" # normal
y3 = "sienna" # dark

g1 = "MintCream" # bright
g2 = "DarkGrey" # normal
g3 = "SlateGray" # dark



# DRAWING

# color code
colors = [
    [wh, bl, wh],
    [wh, bl, wh],
    [wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh],
  	[wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh],
		[wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh],
  	[wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh],
  	[wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh],
  	[wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh, bl, wh],
  	[wh, bl, wh],
  	[wh, bl, wh, bl, wh],
  	[wh, bl, wh],
  	[wh],
  	[wh],
  	[wh, gr3, wh, gr3, wh, gr3, wh, sk3, wh, sk3, wh, gr3, wh, gr3, wh, gr3, wh],
  	[wh, gr3, wh, gr3, wh, gr3, wh, sk3, sk2, sk1, sk3, wh, sk3, sk2, sk1, sk3, wh, gr3, wh, gr3, wh, gr3, wh],
		[wh, gr3, wh, gr3, wh, gr3, wh, sk3, sk2, sk1, sk3, wh, sk3, sk2, sk1, sk3, wh, gr3, wh, gr3, wh, gr3, wh],
  	[wh, gr3, wh, gr3, gr2, gr3, wh, sk3, sk2, sk1, sk3, wh, sk3, sk2, sk1, sk3, wh, gr3, wh, gr3, gr2, gr3, wh],
  	[wh, gr3, wh, gr3, wh, sk3, sk2, sk1, sk3, wh, sk3, sk2, sk1, sk3, wh, gr3, wh, gr3, wh],
  	[wh, gr3, gr2, gr3, wh, gr3, wh, gr3, wh, bl3, wh, gr3, gr2, gr3, wh, gr3, wh, gr3, wh],
  	[wh, gr3, gr2, gr3, wh, gr3, wh, gr3, gr1, gr3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh, gr3, gr2, gr3, wh, gr3, wh, gr3, gr1, gr3, wh],
  	[wh, gr3, wh, gr3, gr1, gr3, wh, gr3, wh, gr3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh, gr3, wh, gr3, gr1, gr3, wh, gr3, wh, gr3, wh],
  	[wh, gr3, gr1, gr3, wh, gr3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh, gr3, gr1, gr3, wh, gr3, wh],
  	[wh, gr3, wh, gr3, gr2, gr3, wh, bl3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh, gr3, wh, gr3, gr2, gr3, wh, bl3, wh],
  	[wh, gr3, wh, gr3, gr2, gr3, bl3, bl2, bl1, bl3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh, gr3, wh, gr3, gr2, gr3, bl3, bl2, bl1, bl3, wh],
  	[wh, bl3, gr3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh, bl3, gr3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh],
  	[wh, bl3, bl2, bl1, bl3, wh, gr3, bl3, y2, y1, bl3, wh, bl3, bl2, bl1, bl3, wh, bl3, bl2, bl1, bl3, wh, gr3, bl3, y2, y1, bl3, wh],
  	[wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, gr3, wh, gr3, y3, wh, bl3, bl2, bl1, bl3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, gr3, wh, gr3, y3, wh],
  	[wh, bl3, y2, y1, bl3, wh, gr3, wh, g3, wh, bl3, y2, y1, bl3, wh, gr3, wh],
  	[wh, y3, wh, bl3, wh, g3, g2, g1, g3, wh, y3, wh, bl3, wh],
  	[wh, bl3, bl2, bl1, bl3, wh, g3, g2, g1, g2, g3, wh, bl3, bl2, bl1, bl3, wh],
  	[wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh, g3, g2, sk3, g2, sk3, wh, bl3, bl2, bl1, bl3, bl2, bl1, bl3, wh],
  	[wh, bl3, y2, y1, bl3, wh, sk3, sk2, sk3, sk2, sk3, wh, bl3, y2, y1, bl3, wh],
  	[wh, y3, wh, sk3, sk2, sk1, sk3, sk1, sk3, wh, y3, wh],
  	[wh, sk3, sk2, sk1, sk3, sk1, sk3, wh],
  	[wh, g3, sk2, sk1, sk3, g1, sk3, sk1, sk3, wh],
  	[wh, g3, g2, g3, sk1, sk3, g1, sk3, sk1, g3, wh],
  	[wh, g3, g2, g3, g2, g1, g3, g1, g3, wh],
  	[wh, g3, g2, g1, g3, g2, g1, g3, g2, g1, g3, wh],
  	[wh, g3, g2, g1, g3, g2, g1, g3, g2, g1, g3, wh],
  	[wh, g3, g2, g1, g3, wh],
  	[wh, g3, g2, g1, g3, wh],
  	[wh, g3, g2, g1, g3, wh],
  	[wh, g3, g2, g1, g3, wh],
  	[wh, g3, g2, g1, g3, g1, g3, wh],
  	[wh, g3, sk2, sk1, g3, wh],
  	[wh, sk3, wh],
  	[wh, sk3, sk2, sk1, sk3, wh],
  	[wh, sk3, sk2, sk1, sk3, wh],
  	[wh, sk3, sk2, sk1, sk2, sk1, sk3, wh],
  	[wh, sk3, sk2, sk1, sk3, wh],
  	[wh, sk3, sk2, sk1, sk3, sk1, sk3, wh],
  	[wh, sk3, sk2, sk1, sk3, sk1, sk3, wh],
  	[wh, sk3, sk2, sk1, sk2, sk3, wh],
  	[wh, sk3, sk2, sk3, sk2, sk1, sk2, sk3, wh],
  	[wh, sk3, sk2, sk1, bl, sk1, bl, sk1, sk2, sk3, wh],
  	[wh, y3, sk2, sk1, bl, sk1, bl, sk1, sk3, wh],
  	[wh, y3, y2, y3, sk2, sk1, sk3, wh],
  	[wh, y3, y2, y3, sk2, sk1, y3, sk1, y3, sk1, sk3, wh],
  	[wh, y3, y2, y3, sk2, sk1, y3, sk1, y3, sk1, sk3, wh],
		[wh, y3, y2, y3, sk2, sk1, y3, sk1, sk3, wh],  
  	[wh, y3, y2, y3, y1, y3, wh],
  	[wh, y3, y2, y1, y3, wh],
  	[wh, y3, y2, y1, y3, wh],
  	[wh, y3, y2, y3, wh],
  	[wh, y3, y2, y3, wh],
  	[wh, y3, wh],
]

# times per color
numbers = [
    [17, 4, 37],
  	[21, 1, 36],
    [2, 1, 4, 3, 2, 1, 5, 4, 1, 1, 3, 1, 4, 4, 6, 1, 3, 1, 3, 1, 2, 4, 1],
    [2, 1, 3, 1, 3, 1, 1, 1, 4, 1, 3, 1, 1, 1, 3, 1, 3, 1, 10, 1, 3, 1, 3, 1, 1, 1, 5],
		[2, 1, 3, 1, 3, 1, 1, 1, 4, 1, 3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 10, 1, 3, 1, 3, 1, 1, 1, 5],
  	[2, 1, 3, 1, 3, 1, 1, 1, 4, 1, 3, 1, 1, 1, 2, 1, 1, 1, 2, 5, 6, 1, 3, 1, 3, 1, 1, 5, 1],
  	[2, 1, 3, 1, 3, 1, 1, 2, 3, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 6, 1, 3, 1, 3, 1, 1, 1, 3, 1, 1],
  	[1, 4, 2, 3, 2, 1, 1, 2, 2, 4, 1, 1, 1, 1, 3, 1, 2, 3, 7, 4, 1, 3, 3, 3, 2],
  	[2, 1, 55],
  	[2, 1, 20, 1, 34],
  	[3, 2, 53],
  	[58],
  	[58],
  	[7, 1, 1, 1, 2, 1, 10, 6, 1, 6, 9, 1, 1, 1, 2, 1, 7],
  	[7, 1, 1, 1, 2, 1, 10, 1, 2, 2, 1, 1, 1, 2, 2, 1, 9, 1, 1, 1, 2, 1, 7],
  	[7, 1, 1, 1, 1, 2, 10, 1, 1, 3, 1, 1, 1, 1, 3, 1, 9, 1, 1, 1, 1, 2, 7],
  	[6, 1, 2, 2, 1, 1, 10, 1, 1, 1, 2, 2, 1, 1, 1, 2, 9, 1, 2, 2, 1, 1, 7],
  	[5, 2, 2, 4, 10, 1, 1, 2, 1, 2, 1, 1, 2, 1, 8, 2, 2, 4, 7],
  	[4, 1, 1, 1, 2, 1, 2, 3, 7, 14, 6, 1, 1, 1, 2, 1, 2, 3, 5],
  	[3, 1, 1, 3, 2, 1, 1, 1, 2, 1, 6, 1, 2, 3, 2, 2, 3, 1, 5, 1, 1, 3, 2, 1, 1, 1, 2, 1, 4],
  	[3, 2, 1, 1, 1, 1, 1, 1, 2, 3, 6, 1, 2, 3, 2, 2, 3, 1, 5, 2, 1, 1, 1, 1, 1, 1, 2, 3, 4],
  	[6, 2, 1, 2, 2, 1, 8, 1, 2, 3, 2, 2, 3, 1, 8, 2, 1, 2, 2, 1, 6],
  	[5, 1, 1, 2, 1, 1, 2, 3, 6, 1, 2, 3, 2, 2, 3, 1, 7, 1, 1, 2, 1, 1, 2, 3, 4],
  	[5, 1, 1, 1, 1, 2, 2, 1, 2, 2, 4, 1, 2, 4, 1, 2, 3, 1, 7, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2],
  	[4, 3, 2, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 2, 4, 1, 2, 3, 1, 6, 3, 2, 1, 1, 1, 1, 3, 1, 1, 1, 1],
  	[2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 4, 1, 2, 10, 1, 4,2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2],
  	[1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3, 6, 1, 2, 10, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3, 4],
  	[2, 2, 1, 2, 2, 1, 1, 11, 14, 4, 2, 1, 2, 2, 1, 1, 9],
  	[4, 3, 2, 3, 10, 1, 2, 10, 1, 6, 3, 2, 3, 8],
  	[7, 2, 1, 2, 2, 8, 1, 7, 1, 4, 1, 9, 2, 1, 2, 2, 6],
  	[6, 1, 1, 1, 3, 1, 1, 1, 7, 1, 1, 6, 1, 5, 8, 1, 1, 1, 3, 1, 1, 1, 5],
  	[7, 2, 1, 2, 2, 8, 2, 6, 1, 5, 1, 8, 2, 1, 2, 2, 6],
  	[9, 3, 9, 1, 2, 6, 1, 6, 1, 9, 3, 8],
  	[20, 1, 1, 8, 1, 6, 1, 20],
  	[20, 1, 1, 3, 5, 1, 3, 4, 1, 19],
  	[19, 1, 1, 1, 2, 1, 9, 1, 2, 2, 19],
  	[19, 1, 2, 2, 1, 9, 3, 1, 1, 19],
  	[19, 1, 2, 1, 1, 1, 9, 1, 1, 2, 1, 19],
  	[19, 1, 2, 1, 1, 1, 9, 1, 1, 2, 1, 19],
  	[19, 1, 2, 16, 1, 19],
  	[19, 1, 2, 16, 1, 19],
  	[20, 1, 2, 14, 1, 20],
  	[20, 1, 2, 14, 1, 20],
  	[21, 2, 2, 1, 6, 3, 2, 21],
  	[23, 3, 2, 4, 3, 23],
  	[25, 8, 25],
  	[23, 2, 1, 7, 2, 23],
  	[22, 1, 2, 10, 1, 22],
  	[21, 1, 2, 3, 2, 7, 1, 21],
  	[21, 1, 2, 12, 1, 21],
  	[20, 1, 3, 2, 5, 6, 1, 20],
  	[20, 2, 2, 1, 1, 11, 1, 20],
  	[19, 1, 4, 13, 1, 1, 19],
  	[19, 1, 1, 1, 2, 1, 13, 1, 19],
  	[19, 1, 4, 2, 2, 6, 2, 1, 1, 1, 19],
  	[20, 3, 1, 2, 2, 6, 2, 1, 1, 20],
  	[20, 1, 1, 1, 1, 13, 1, 20],
  	[20, 1, 1, 1, 1, 2, 1, 8, 1, 1, 1, 20],
  	[20, 1, 1, 1, 1, 3, 1, 6, 1, 2, 1, 20],
  	[20, 1, 1, 1, 1, 5, 4, 4, 1, 20],
  	[20, 1, 2, 6, 4, 5, 20],
  	[20, 1, 3, 13, 1, 20],
  	[21, 1, 3, 11, 1, 21],
  	[21, 2, 12, 2, 21],
  	[23, 2, 8, 2, 23],
  	[25, 8, 25],
]

# looping through colors
for i in range(len(colors)):
    drawRow(colors[i], numbers[i])
    
t = input()