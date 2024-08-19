# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:59:33 2024

@author: Kaviyarasan PR
"""

"""User defined the function: user going to define the function by using built in or library functions"""

""" function definition: function arguments(parameters), return type, function call, function name, function prototype"""

""" formal and actual arguments"""

""" actual arguments- used to call the function"""
""" formal arguments- The name which we use in the function name """

""" multiple return is possible"""

""" write meaningful name to the function name """


def cal_sum(x,y):
    s=x+y
    return s
a=10
b=10
print(cal_sum(a,b))

def square(x):
    sq=x**2
    return sq
a=754

print(square(a))

def mul(x,y):
    s=x*y
    return s
a=10
b=72
print(mul(a,b))

def check_number(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"

result = check_number(5)
print(result) 

result = check_number(-2)
print(result) 

result = check_number(0)
print(result)


def pos_fun(i, f, st):
    st1 = st.upper()
    su1 = i+f
    
    return su1, st1

i1, f1, st1 = 5, 6.34, 'Ram'
out1, out2 = pos_fun(i1,st1, f1)
print('Function returning multiple values ', out1, out2)


def pos_fun(i, f, st):   
    su1 = i+f
    st1 = st.upper()
    
    return su1, st1

i1, f1, st1 = 5, 6.34, 'Ram'
out1, out2 = pos_fun(i1,st1, f1)
print('Function returning multiple values ', out1, out2)



def pos_fun(i, f, st):   
    su1 = i+f
    st1 = st.upper()
    
    return su1, st1

i1, f1, st1 = 5, 6.34, 'Ram'
out1, out2 = pos_fun(f1,i1,st1)
print('Function returning multiple values ', type(out1), type(out2))


"""Keyword Arguments"""

out_lst2 = pos_fun(i=10, f=20.3, st='Ram')
print(out_lst2)
print(type(out_lst2))

out_lst3 = pos_fun( f=256,i=10, st='Ram')
print(out_lst3)

"""keyword argument we can change the position of the arguments and still it will assign the values correctly"""

"""positional argument follows keyword argument"""


def combination(a,b,c):
    add=a+b
    c= c.upper()
    return add, c

o1,o2= combination(10, b=10, c="kavi")    
print(o1, o2)

o1,o2= combination(a=10, 10, c="kavi")    














