import turtle
import random

n = int(input("Enter the number of repeats : "))

turtle.setup(800, 800)
wn = turtle.Screen()
wn.bgcolor("black")

#Drawing 3 main points
pt = turtle.Turtle()
pt.speed(0)
pt.color("blue")
pt.penup()
pt.right(180)
pt.forward(200)
pt.left(90)
pt.forward(100)
pt.left(90)
pt.dot()
B = pt.pos()
pt.left(60)
pt.forward(500)
pt.dot()
A = pt.pos()
pt.right(120)
pt.forward(500)
pt.dot()
C = pt.pos()
pt.color("red")

#Drawing random point
x = random.randint((int)(B[0]), (int)(C[0]))
y = random.randint((int)(B[1]), (int)(A[1]))
pt.goto(x, y)
pt.dot()

i = 0
while i < n: 
	randomPoint = random.randint(0, 2)
	if (randomPoint == 0):
		pt.goto((x+A[0])/2 , (y+A[1])/2)
		pt.dot()
		x = pt.pos()[0]
		y = pt.pos()[1]
	elif (randomPoint == 1):
		pt.goto((x+B[0])/2 , (y+B[1])/2)
		pt.dot()
		x = pt.pos()[0]
		y = pt.pos()[1]
	else:
		pt.goto((x+C[0])/2 , (y+C[1])/2)
		pt.dot()
		x = pt.pos()[0]
		y = pt.pos()[1]

	i = i + 1



turtle.done()