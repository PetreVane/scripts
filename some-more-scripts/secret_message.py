

import os
import string



#print listdir('/Users/petre/Programare/Nanodegree/Python')
#file_path = os.getcwd()


#print file_list


def rename_files():
    file_list = os.listdir('/Users/petre/Programare/Nanodegree/Python/prank')
    print file_list
    saved_path = os.chdir('/Users/petre/Programare/Nanodegree/Python/prank')
    print 'current working directory is  ' +  (saved_path)
    for file_name in file_list:
	print ('Old name  -' + file_name)
	os.rename(file_name, file_name.translate(None, '0123456789'))
	print ('New name  -' + file_name.translate(None, '0123456789')
        #os.chdir(saved_path)
               
rename_files()  
