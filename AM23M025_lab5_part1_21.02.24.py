# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:12:09 2024

@author: Kaviyarasan PR
"""

"""1. Write a program(WAP) using loops and recursion: 

a) Factorial of n where n is a non negative integer. 

b) For calculating the Nth Fibonacci number.

c) To calculate a^b where a>0, b>=0."""
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))  



def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10


if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms+1):
       print(recur_fibo(i))


a=90
b=2
def power(a,b):
    return a**b
print(power(a,b))

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b - 1)


a = 2
b = 3
result = power(a, b)
print(f"{a}^{b} = {result}")

"""using for loops and while loops"""
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        while(n > 1):
            factorial *= n
            n -= 1
        return factorial
 

num = 5
print("Factorial of",num,"is",factorial(num))

a, b = 0, 1
n = 10

for i in range(n):
    a, b = b, a + b
    print(a)
    
# print(a)


def power_loop(a, b):
    result = 1
    for _ in range(b):
        result *= a
        # print(result)
    return result

a = 5
b = 9

print(power_loop(a,b))

"""2. Query for 2 integers N and M from the user where 0<=N<=100 and 0<=M<=9. 
These will be the inputs to your function. Using recursion, compute the number of times 
the integer M occurs in all non-negative integers less than or equal to N.
example: For N=13 and M=1, count=6 (numbers 1,10,11,12,13)."""


def count_occurrences(N, M):
    def count_in_number(number):
        count = 0
        while number > 0:
            if number % 10 == M:
                count += 1
            number //= 10
        return count
    
    total_count = 0
    for num in range(N + 1):
        total_count += count_in_number(num)
    return total_count

N = int(input("Enter the value of N:"))
M = int(input("Enter the value of M:"))


if not (0 <= N <= 100) or not (0 <= M <= 9):
    print("give valid input")
else:
    count = count_occurrences(N, M)
    print(f"The integer {M} occurs {count} times in all non-negative integers less than or equal to {N}.")

"""3. Programs using lambda function.

a) Given a list of names, use map to create a list where each name is prefixed with "Hello, ".

Example Input: ['Alice', 'Bob', 'Charlie']
Example Output: ['Hello, Alice', 'Hello, Bob', 'Hello, Charlie']"""


list1 = ['Alice', 'Bob', 'Charlie']
greeted_names = list(map(lambda name: f"Hello, {name}",list1))
print(greeted_names)


"""b) Use filter and a lambda function to extract all even numbers from a given list.

Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [2, 4, 6]"""

num=[1, 2, 3, 4, 5, 6]
filtered=list(filter(lambda x : x%2==0,num))
print(filtered)


"""c) Use reduce and lambda to concatenate all strings in a given list.

Example Input: ['Python', 'is', 'awesome']
Example Output: 'Pythonisawesome'"""


from functools import reduce
li=['Python', 'is', 'awesome']


concat= reduce(lambda x, y: x + y, li)
print(concat)





"""4.  Define a class Complex that defines a complex number with attributes r and
 iinary (as we did in the class). Define operators for addition, subtraction, multiplication and 
 division (Do with both operator overloading as well as without overloading). While printing the output, 
 print in the form of complex number form like ( a + ib) """
 
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    # Operator Overloading for Addition
    def __add__(self, o):
        return Complex(self.r + o.r, self.i + o.i)
    
    # Operator Overloading for Subtraction
    def __sub__(self, o):
        return Complex(self.r - o.r, self.i - o.i)
    
    
    def __mul__(self, o):
        r = self.r * o.r - self.i * o.i
        i = self.r * o.i + self.i * o.r
        return Complex(r, i)
    
    
    def __truediv__(self, o):
        denominator = o.r**2 + o.i**2
        r = (self.r * o.r + self.i * o.i) / denominator
        i = (self.i * o.r - self.r * o.i) / denominator
        return Complex(r, i)
    
    def __str__(self):
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        else:
            return f"{self.r} - {abs(self.i)}i"
    

    def add_complex(self, o):
        r = self.r + o.r
        i = self.i + o.i
        return Complex(r, i)
    
    def sub_complex(self, o):
        r = self.r - o.r
        i = self.i - o.i
        return Complex(r, i)
    
    def mul_complex(self, o):
        r = self.r * o.r - self.i * o.i
        i = self.r * o.i + self.i * o.r
        return Complex(r, i)
    
    def div_complex(self, o):
        denominator = o.r**2 + o.i**2
        r = (self.r * o.r + self.i * o.i) / denominator
        i = (self.i * o.r - self.r * o.i) / denominator
        return Complex(r, i)

c1 = Complex(2, 3)
c2 = Complex(4, -5)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)


print("Addition:", c1.add_complex(c2))
print("Subtraction:", c1.sub_complex(c2))
print("Multiplication:", c1.mul_complex(c2))
print("Division:", c1.div_complex(c2))


"""In Python, when you try to convert an object to a string (implicitly or explicitly), 
the __str__ method is automatically called if it's defined for that object's class. 
This is part of Python's object-oriented model.

When you use print() to display an object, 
Python internally calls str() on that object to obtain its string representation. 
Since your Complex class defines the __str__ method, 
Python automatically invokes this method to get the string representation of the object when you use print().

For example, when you write print(c1 + c2), Python internally calls str(c1 + c2). 
Since c1 + c2 results in a Complex object, 
Python calls the __str__ method of that object to obtain its string representation, 
and then prints that string representation.

So, even though you don't explicitly call str() in your code, 
Python internally uses str() to obtain the string representation of objects when needed, 
such as when printing or concatenating strings."""







