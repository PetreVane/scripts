

import os
import string


#path = os.getcwd()
#print path


#saved_path = os.chdir('Users/petre/Programare/Nanodegree/Python/prank')
#print saved_path

#print 'Current working directory is ' + str(saved_path)
#print saved_path


def rename_files():
    file_list = os.listdir('/Users/petre/Programare/Nanodegree/Python/prank')
    print file_list
    saved_path = os.chdir('/Users/petre/Programare/Nanodegree/Python/prank')
    print saved_path
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, '0123456789'))


rename_files()  


