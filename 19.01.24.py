# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:03:21 2024

@author: Kaviyarasan PR
"""

a=8
print(id(a))

a=10
print(id(a))

b=90
print(id(b))


""" concatenation"""
 
s= "kavi"
k= " dinesh"

print(s+k)

print("-"*70)

print('el'in "hello")

print('kavi'in "Kavi")

"""member functions"""

str1= "kaviyarasan,is a good boy"
print(str1.isalpha())
print(str1.isdigit())
print(str1.islower())
print(str1.isalnum())
print(str1.startswith('k'))
print(str1.endswith('san'))
print(str1.upper())
print(str1.capitalize())
print(str1.swapcase())
print(str1.replace('a','f',1))
print(str1.split(","))

""" 1.len(), rstrip(), partition(), str(), ord(), index()
    2. given a str, WAP to split them at the following \,\\, blank space
    3. db split() and .......
"""

"""console input and output"""
a= input("enter a number")
b= input("enter a number")
c=a+b
print(c)
c= int(a)+int(b)
print(c)

"""str to integer typecasting"""
str='109200'
num= int(str)
print(num+10)
print(type(num))
print(type(str))

""" spliting two numbers"""
a,b= input("enter the two numbers").split(' ')
c= int(a)+int(b)
print(c)

"""enter multiple data"""
data = input("enter the name, age, salary:").split()
name= data[0]
print(name)


print(data[0] + '\t')






























