

import turtle

def draw_something(something):
	for i in range(1, 5):
		something.forward(230)
		something.right(90)

def drawing():
	window = turtle.Screen()
	window.bgcolor('#F5F6F7')


	peter = turtle.Turtle()
	peter.shape('turtle')
	peter.speed(15)



	peter.color('red')
	for i in range (1, 51):
		peter.circle(60)
		peter.left(3.5)

	peter.color('#49B9FB')
	peter.backward(150)
	for i in range(1,91):
		peter.circle(90)
		peter.left(2)

	#peter.circle(90)
	
	
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('#30EC6E')
	brad.speed(50)
	brad.pensize(0.05)
	brad.forward(135)

	for i in range(1,46):
		draw_something(brad)
		brad.right(1)
	#peter.circle(60)

	peter.color('pink')
	peter.pensize(1.5)
	peter.forward(-175)
	for i in range(1,85):
		peter.circle(170)
		peter.left(2)


	


	window.exitonclick()

drawing()
