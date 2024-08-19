# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 09:16:44 2024

@author: Kaviyarasan PR
"""

""" In 3D graphics STl files are used to convert the design into code"""

""" any opening of the file, we should close it. """

""" popular format -.csv"""



msg1="Hi. This is kavi."
msg2= " how are you?"
msg3=23423849235
f= open("message.txt",'w')

f.write(msg1)
f.write(msg2)

f.close()
f=open("message.txt",'r')
content= f.read()
print(content)
print(content[0])
print(type(content))
f.close()

"""suppose we have a file, we need to add some more text --for that we have apppend mode"""
f= open("message.txt",'a')
f.write(str(msg3))
f=open("message.txt",'r')
content= f.read()
print(content)
f.close()



""" import os and import shutil """



import os
import shutil

print(os.name)
print(os.getcwd())
print(os.listdir('.'))

""" . (dot ) will give you the working directory . double dot(..) will go one level higher"""

""" how to use join. """

import csv

with open('test_csv1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Header names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and handles {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    
"""hw- JSON- JavaScript Object Notation vs dictionary """












