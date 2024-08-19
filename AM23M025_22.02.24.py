# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:57:37 2024

@author: Kaviyarasan PR
"""
class Base():
    def __init__(self, name, roll, marks):
        self.name=name
        self._roll= roll
        self.__marks=marks
class Derived(Base):
    def __init__(self,name, roll, marks, name1, roll1, marks1):
        super().__init__(name, roll, marks)
        self.name1=name1
        self._roll1=roll1
        self.__marks1=marks1
        
        # self.name="newname"
        # self._roll= 29342
        self.__marks=21
    def printderived(self):
        print(self.name, self._roll, self.__marks)
        print(self.name1, self._roll1, self.__marks1)


d1 = Derived('Ram', 1234, 85, 'Raman', 4356, 76)
d1.printderived()
d1.name1 = 'Ramamoorthy'
d1._roll1 = 8890
d1.__marks1 = 10 
d1.__marks = 100 
d1.printderived()

"""multilevel inheritence vs multiple inheritance"""

""" class Derived (Base1,Base2)- derived form two base classes"""

# class Derived1(Derived):
#     def __init__(self,name):
#         print("derived2 class")

# d2=Derived1()
# print(d2)


class Grandparent:
    def __init__(self):
        print("Grandparent constructor")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

# Creating an instance of the Child class
c = Child()


class Base1:
    def method_base1(self):
        print("Method from Base1")

class Base2:
    def method_base2(self):
        print("Method from Base2")

class Derived(Base1, Base2):
    def method_derived(self):
        print("Method from Derived")

d = Derived()


d.method_base1()
d.method_base2()

d.method_derived()


class Base1:
    def __init__(self):
        print("Constructor of Base1")

class Base2:
    def __init__(self):
        print("Constructor of Base2")

class Derived(Base1, Base2):
    def __init__(self):
        super().__init__()  
        Base1.__init__(self)
        Base2.__init__(self)
        print("Constructor of Derived")

d = Derived()


""" _ called as protected 
    __  called as private """
    
""" to create front end  or GUI we use tk and qt library """

""" HW: use the concept of containership"""

""" containership is like nested structures """


""" HW: class variables and methods""" 
""" in C it is like static"""

"""what is dynamic creation of attributes"""






























