
import urllib


def read_text():
	quotes = open("/Users/petre/Programare/Python/movie_quotes.txt")
	content_to_scan = quotes.read()
	#print content_to_scan
	quotes.close()




	def check_profanity(text_to_check):
		connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text_to_check)
		output = connection.read()
		#print output
		connection.close()

		if 'true' in output:
			print 'This document has some innapropriate words'

		elif 'false' in output:
			print 'This document is ready to go'
		else:
			print 'this document could not be scanned!'


	check_profanity(content_to_scan)

read_text()

def testing():
	if read_text():
		print ("it's working")
	else:
		print ("it's not working")

testing()
