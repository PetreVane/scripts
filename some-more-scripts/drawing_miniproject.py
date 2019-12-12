
import turtle

def draw_art(name):
	for i in range(1, 8):
		name.forward(50)
		name.left(5.5)
		name.fill(True)
		name.pensize(2.5)
		name.color('#c43a3a', '#e26666')
		

def draw_circle(name):
	for m in range(1, 9):
		name.circle(30)
		name.left(2.5)
		name.color('#ffe95b')


def drawing_flower():
	window = turtle.Screen()
	window.bgcolor('#f7ffdd')
	peter = turtle.Turtle()
	peter.shape('arrow')
	peter.speed(155)

#drawing the petals 

	for n in range(1,29):
		draw_art(peter)
		peter.setpos((10, 10))

#drawing the middle thing of the flower

	for n in range(1, 19):
		draw_circle(peter)
		peter.setpos((10, 10))


	window.exitonclick()

drawing_flower()


