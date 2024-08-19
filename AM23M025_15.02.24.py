# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 10:02:01 2024

@author: Kaviyarasan PR
"""


def summ(*kavi):
    s = 0
    for arr in kavi:
        s += sum(arr)
    return s

arr = [90, 98, 100]
print(summ(arr))

def kwvar_arg(**kavi):
    for k,v in kavi.items():
        print(k,v)
        
kwvar_arg(i = 10)
kwvar_arg(i = 10, j = 20.34)
kwvar_arg(i = 10, j = 20.34, k = 'Ram')


def summ(**kavi):
    s = 0
    for arr in kavi:
        s += sum(arr)
    return s

arr = [90, 98, 100]
print(summ(arr))


""" default argument """

"""overwriting the default argument will change the default to False """
def kavi(ph=6379103123):
    if ph==6379103123:
        print("the phone num is correct")
    else:
        print("the phone num is not correct")
kavi()
kavi(4582455622)



def ex(p_arg1, p_arg2, k_arg1, k_arg2, cond= "thambi tea innu varala"):
    print("Positional arguments:", p_arg1, p_arg2)
    print("Keyword arguments:", k_arg1, k_arg2)
    print("default arguments:", cond)


# ex(10, 10000)

# ex(10, 1000, k_arg1="kavi")

ex(700, 75000, k_arg1="dinesh", k_arg2="valentine")


""" RECURSIVE FUNCTION"""

def printnum(n):
    if n>0:
        print(n)
        printnum(n-1)
printnum(10)

def summation(n):
    if n == 1:
        return 1
    else:
        return n + summation(n - 1)

print(summation(80))


def summ(n):
    total=0
    if n>0:
        for i in range(n+1):
            total+=i
    print(total)
summ(5)

"""Do the factorial of any given value ’n’ using recursion 
HW: Series summation - odd factorial, even factorial, 
exp(x), sin(x), etc. using recursion 
"""























