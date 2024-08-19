# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 08:03:28 2024

@author: Kaviyarasan PR
"""
"""using lambda function how to sort in reverse the dictionary (sort by keys and values)"""

average= lambda a,b: (a+b)/2
print(average(90,12))


lst= [1,2,3,4,5,6]
lst2=map(lambda x : x**2,lst) 
print(lst2)
print(type(lst2))
print(list(lst2))
"""square brackets are used for indexing or list comprehension, 
but for the map() function, parentheses are needed."""

class Student:
    def __init__(self,n='', r='',s=1):
        self.name =n
        self.rollno=r
        self.sem=s
        
    def printout(self):
        print(self.name, self.rollno,self.sem)
    
    def change(self,x='',y='',z=''):
        self.name=x
        self.rollno=y
        self.sem=z
        
s2=Student('ram',"am23m1223",3) #object instantiation - assigning values to the objects
s2.printout()

"""self is the fourth argument, s2 is the self argument which is called over init function"""


""""__INIT__ IS THE CONSTRUCTOR"""




s3=Student("kaviyarasan","am23m025", 2)
s3.printout()

s4=Student()
s4.change("dinesh","am23m022", 2)
s4.printout()

print(s4.name)
"""it is not supposed to print it ----if we write it in c++ we dont get the data (public and private)--data protection"""

class Student_1:
    def datainput(self,n, r,s):
        self.name =n
        self.rollno=r
        self.sem=s
        
    def printout(self):
        print(self.name, self.rollno,self.sem)

s5=Student_1()
s5.datainput("kavi","am23m025", 4)
s5.printout()




class StudentDetail:
 
 #Constructor
     def __init__(self, n='R', r=1, s=1):
         self.name = n
         self._rollno = r
         self.__sem = s
#Printing the data
     def printout(self):
         print('name = ', self._name, ", " , 'roll no = ', self._rollno, ", " , 'sem = ', self._sem)
 
 #destructor
     def __del__(self):
         print('Del obj' + str(self))
 
s1 = StudentDetail()
s1.printout()
s1 = StudentDetail('Ram')
s1.printout()
s1 = StudentDetail('Raman', 23)
s1.printout()
s1 = StudentDetail('Ramana', 23, 5)
s1.printout()

""" single underscore: notionally private data"""
""" thuderscore: the data is actually private but we can't print it outside the class"""


print(s1.sem)


class StudentDetail:
       def get_sem(self):
           return self.__sem

       def set_sem(self, new_sem):
           self.__sem = new_sem

s1 = StudentDetail()
print(s1.get_sem())  # Accessing sem using a method
s1.set_sem(6)  # Modifying sem using a method
print(s1.get_sem())  # Accessing sem after modification


class StudentDetail:
    # Constructor
    def __init__(self, n='R', r=1, s=1):
        self.name = n
        self._rollno = r
        self.__sem = s

    # Printing the data
    def printout(self):
        print('name = ', self.name, ", ", 'roll no = ', self._rollno, ", ", 'sem = ', self.__sem)

    # Destructor
    def __del__(self):
        print('Del obj' + str(self))

s1 = StudentDetail()
s1.printout()

# Accessing the __sem attribute using name mangling
print(s1._StudentDetail__sem)


