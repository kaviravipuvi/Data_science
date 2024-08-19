# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:01:45 2024

@author: Kaviyarasan PR
"""

""" you have thuderscore variable inside the class and we are trying to access that variable outside 
the class and what type it would be when it is outside the class?"""

class Complex:
    def __init__(self, r=0, im=0):
        self._real = r
        self._imag = im
        print(self)
        
    #Addition of two complex numbers using a method
    def add_comp(self, other):
        c = Complex()
        c._real = self._real + other._real
        c._imag = self._imag + other._imag
        return c
    
    #Addition of two complex numbers using operator overloading
    def __add__(self, other):
        c = Complex()
        c._real = self._real + other._real
        c._imag = self._imag + other._imag
        return c
    def __sub__(self, other):
        c=Complex()
        c._real= self._real-other._real
        c._imag=self._imag- other._imag
        return c 
        
    def print_comp(self):
        print('real = ', self._real, 'imag = ', self._imag)
    
c1 = Complex(4.5, 5.45)
c2 = Complex(3.5, 8.45)
# c3 = Complex()
# c3.print_comp()
# c3 = c1.add_comp(c2)
c1.print_comp()
c2.print_comp()


c3 = c1 - c2 
c3.print_comp()

c4 = c1 + c2 
c4.print_comp()





"""HW :check the possibility of function overloading in python"""