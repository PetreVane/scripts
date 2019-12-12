





import webbrowser
import time 

def take_a_break():
	counting = 0
	while counting < 3:
		time.sleep(5)
		webbrowser.open('https://www.youtube.com/watch?v=drXNPy23Xco')
		counting = counting + 1
		print ' the program has startet ' + time.ctime()

take_a_break() 







