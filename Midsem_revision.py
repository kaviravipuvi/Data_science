# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:53:11 2024

@author: Kaviyarasan PR
"""

# def PrintNum(n): 
#     if n > 0:        
#         PrintNum(n-1) 
#         print(n)

# PrintNum(2)

# def sum_n(n):
#     if n==0:
#         return 1
#     if n>0:
#          s = n*sum_n(n-1)
#          print(s)
#          return s
# sum_n(5)


import math

# def odd_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * odd_factorial(n - 2)

# def even_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * even_factorial(n - 2)

# def exponential(x, n):
#     if n == 0:
#         return 1
#     else:
#         return (x ** n) / math.factorial(n)

# def sine(x, n):
#     if n == 0:
#         return x
#     else:
#         sign = (-1) ** n
#         return sign * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

# # # Example usage:
# # print("Odd Factorial of 5:", odd_factorial(5))
# # print("Even Factorial of 6:", even_factorial(6))
# print("Exponential (e^2) with 5 terms:", exponential(1, 1))
# print("Sine of pi/2 with 5 terms:", sine(math.pi/2, 5))




# class MyClass:
#     class_variable = 10  # Class variable shared across all objects
    
#     @classmethod
#     def class_method(cls):
#         print("This is a class method")
#         print("Accessing class variable:", cls.class_variable)

# # Example usage:
# print("Accessing class variable directly:", MyClass.class_variable)

# obj1 = MyClass()
# obj2 = MyClass()

# # Accessing class variable through objects (although it's usually accessed through class name)
# print("Accessing class variable through obj1:", obj1.class_variable)
# print("Accessing class variable through obj2:", obj2.class_variable)

# # Modifying class variable through one object affects all objects
# obj1.class_variable = 20
# print("Class variable after modification through obj1:", obj1.class_variable)
# print("Class variable through obj2:", obj2.class_variable)

# # Calling class method
# MyClass.class_method()



# class Passbook:
#     pass

# p1 = Passbook()
# p1._name = 'Raman'
# p1._number = 123

# # Now, p1 has two attributes: _name and _number, which were dynamically created.
# print("Name:", p1._name)
# print("Number:", p1._number)



# class Department:
#     def __init__(self, name):
#         self.name = name

# class Faculty:
#     def __init__(self, name, department):
#         self.name = name
#         self.department = department  # Faculty has a department

# class Student:
#     def __init__(self, name, department):
#         self.name = name
#         self.department = department  # Student has a department

# # Creating departments
# physics_dept = Department("Physics")
# math_dept = Department("Mathematics")

# # Creating faculty members
# professor_john = Faculty("John Doe", physics_dept)
# professor_alice = Faculty("Alice Smith", math_dept)

# # Creating students
# student_alex = Student("Alex Johnson", physics_dept)
# student_emily = Student("Emily Brown", math_dept)

# # Accessing information
# print("Faculty member:", professor_john.name)
# print("Faculty member's department:", professor_john.department.name)

# print("Student:", student_alex.name)
# print("Student's department:", student_alex.department.name)




# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

# # You cannot instantiate an abstract class
# # shape = Shape()  # This will raise an error

# # But you can instantiate a subclass
# rectangle = Rectangle(5, 4)
# print("Area:", rectangle.area())
# print("Perimeter:", rectangle.perimeter())



# lst = [10, 20, 30]

# # Get the iterator object by calling __iter__()
# iterator = lst.__iter__()

# # Keep calling __next__() until StopIteration exception is raised
# while True:
#     try:
#         # Get the next element using __next__()
#         ele = iterator.__next__()
#         # Process the element
#         print(ele)
#     except StopIteration:
#         # Exit the loop when StopIteration exception is raised
#         break


# import numpy as np

# arr = np.arange(1.9, 100, 0.1)  # [0, 2, 4] (excluding 5)
# lin = np.linspace(0, 100, 100)  # [0.  2.5 5. ] (including 0 and 5)

# print(arr)
# print(lin)



import numpy as np
import matplotlib.pyplot as plt



# x = np.linspace(-5, 5, 100)
# y = x**2
# # plt.plot(x,y,'o--')
# # plt.plot(x, y, 'o--', color='red', lw = 10, ms = 2)

# plt.figure(figsize=(6,3))
# plt.plot(x, y, 'o-', color='red', lw = 1.5, ms = 2, label = 'par. crv')
# plt.xlabel('parameter')
# plt.ylabel('curve')
# plt.legend(loc='upper right', fontsize = 10)



# #using subplots
# x = np.arange(-2.0, 2.0, 0.01)
# y = x ** 2
# z= x**3
# #Default is single figure
# #fig, ax = plt.subplots()
# #single axis
# fig, axes = plt.subplots(2, 2, figsize = (4,4))
# ax = axes[0, 1] 
# ax.plot(x, y)
# ax = axes[1, 1] 
# ax.plot(x,z)

# ax.set_xlabel('new x-label')
# ax.set_ylabel('new y-label')
# ax.set_title('Single axis plot')
# # ax.set(xlabel='x vlues', ylabel='y values',
# # title='Explicit function y = f(x)')
# ax.grid()

# plt.tight_layout()
# plt.show()




# t = np.arange(-2.0, 2.0, 0.1)
# x = t
# y = t ** 2
# z = t ** 3
# r= t**4
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x, y, z)
# ax = fig.add_subplot(221, projection='3d')
# ax.plot(x,y,r)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# ax.set_title('Parametric space curve t, t**2, t**3')
# plt.tight_layout()



# x = np.arange(-2.0, 2.0, 0.1)
# y = np.arange(-2.0, 2.0, 0.1)
# # The following will print a 3D surface
# X,Y=np.meshgrid(x,y) #Forming MeshGrid
# Z = X **2 + Y ** 2
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# plt.show()


# # Create a bytes object from a sequence of integers
# byte_data = bytes([65, 66, 67, 68, 69])  # ASCII values for 'ABCDE'

# # Print the bytes object
# print(byte_data)  # Output: b'ABCDE'

# # Access individual bytes in the bytes object
# print(byte_data[0])  # Output: 65

# # Iterate over the bytes object
# for byte in byte_data:
#     print(byte)

# # Create a bytes object from a string
# string_data = "Hello"
# byte_string = bytes(string_data, 'utf-8')

# # Print the bytes object
# print(byte_string)  # Output: b'Hello'

# # Access individual bytes in the bytes object
# print(byte_string[0])  # Output: 72 (ASCII value for 'H')

# # Iterate over the bytes object
# for byte in byte_string:
#     print(byte)





# result = 2 + 3 * 4 ** 2 - 10 / 2
# print(result)  # Output: 42.0



# # Convert int to float
# int_value = 10
# float_value = float(int_value)
# print(float_value)  # Output: 10.0

# # Convert float to int
# float_number = 7.8
# int_number = int(float_number)
# print(int_number)  # Output: 7

# # Convert int to complex
# int_num = 5
# complex_num = complex(int_num)
# print(complex_num)  # Output: (5+0j)

# # Convert complex to float
# complex_num = 3 + 4j
# float_part = float(complex_num.real)
# print(float_part)  # Output: 3.0




# # Sample data (modify as needed)
# x = np.array([10.0, 15.0, 22.5, 7.0])
# y = np.array([3.0, 2.0, 1.5, 4.0])

# # Calculate quotient and remainder
# quotient = np.round(x / y, decimals=3)  # Round to two decimal places
# remainder = x % y

# # Print results
# print("Quotient (rounded to 2 decimals):")
# print(quotient)
# print("\nRemainder:")
# print(remainder)

# x =6
# y = 4
# # z= x/y
# sol = round(x/y, 3)
# print(sol)

# str1="Raman"
# start=5
# end=3

# # print(str1[start : end])
# # print(str1[start : ])
# # print(str1[ :end])
# print(str1[-start :])
# print(str1[:-end])


# text = "   This has trailing spaces  "
# trimmed_text = text.rstrip()  # trimmed_text will be "   This has trailing spaces"
# trimmed_text2 = text.rstrip("T")  # trimmed_text2 will be "   This has trailing spaces"
# print(trimmed_text)
# print(trimmed_text2)





# text = "Name: Alice, Age: 30"
# parts = text.partition(": ")  # parts will be ("Name", ": ", "Alice, Age: 30")
# print(parts)




# name = "Alice"
# age = 30
# print(name, age, sep="-", end="s")  # Output: Alice-30


# List with at least one True element
# data1 = [True, False, True, True]
# print(any(data1))  # Output: True

# # List with all False elements
# data2 = [False, False, False]
# print(any(data2))  # Output: False

# # Empty list
# data3 = []
# print(any(data3))  # Output: False

# # String with at least one non-zero character (considered True)
# data4 = "Hello"
# print(any(data4))  # Output: True

# # String with only spaces (considered False)
# data5 = " "
# print(any(data5))  # Output: False

# # List with all True elements
# data1 = [True, True, True]
# print(all(data1))  # Output: True

# # List with at least one False element
# data2 = [True, False, True]
# print(all(data2))  # Output: False

# # Empty list
# data3 = []
# print(all(data3))  # Output: True (considered True for empty iterables)

# # String with all non-zero characters (considered True)
# data4 = "Hello"
# print(all(data4))  # Output: True

# # String with a space (considered False)
# data5 = " Python "
# print(all(data5))  # Output: False




# tup= (8,)
# print(type(tup))

# t= (8*2)

# x=()
# print(type(x))


# Example using pass
# for i in range(5):
#     if i == 3:
#         print("Skipping number 3")
#         pass  # Do nothing and continue to the next iteration
#     print(i)

# # Example using break
# for i in range(5):
#     if i == 3:
#         print("Breaking the loop at number 3")
#         break  # Exit the loop immediately
#     print(i)


# tup1 = (1, 2)
# print(tup1[1:3])