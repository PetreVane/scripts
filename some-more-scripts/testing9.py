

import os
import string 



file_list = os.listdir('/Users/petre/Programare/Nanodegree/Python/prank')
print file_list
saved_path = os.chdir('/Users/petre/Programare/Nanodegree/Python/prank')

print saved_path
print 'current working directory is  ' + str(saved_path)