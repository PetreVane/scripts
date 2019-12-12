

import turtle 

def draw_something(something):
	for i in range(1, 5):
		something.forward(100)
		something.right(90)


def draw_art():
	window = turtle.Screen()
	window.bgcolor('red')
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('yellow')
	brad.speed(8)

	for i in range(1,37):
		draw_something(brad)
		brad.right(10)



	window.exitonclick()

	#Creating the secong turtle
'''
	#angie = turtle.Turtle()
	angie.color('blue')
	angie.shape('arrow')
	angie.pensize(5)
	angie.circle(50)
'''
		

draw_art()


'''
def draw_triangle():

	ioana = turtle.Turtle()
	ioana.shape('arrow')
	ioana.color('green')
	ioana.forward(45)
	ioana.right(45)
	ioana.forward(45)


draw_triangle()
#window.exitonclick()
'''

