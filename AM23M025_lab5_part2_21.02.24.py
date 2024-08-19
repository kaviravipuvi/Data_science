# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:30:27 2024

@author: Kaviyarasan PR
"""

"""5. WAP to implement a class called "Bank_Account" representing a person's bank account.
The class should have the following attributes: account_holder_name (str), account_number(int), address (str) and balance (float).
The class should have methods to implement the following:
    deposit - Deposits a given amount into the account
    withdraw - Withdraws a given amount from the account
    check_balance - To get the current balance
    update_details - To update the name and address from the user and displays a message indicating successful update
    display_details - To display the details of the account."""
    
class Bank_account():
    def __init__(self, a_h_n, a_n, add, bal):
        self.a_h_n= str(a_h_n)
        self.a_n= int(a_n)
        self.add= str(add)
        self.bal=float(bal)
    
    def deposit(self, amount):
        self.bal += amount
        print(f"Deposit successful. Balance is now {self.bal}")
                
        
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.bal:
            return "Insufficient balance"
        else:
            self.bal -= withdraw_amount
            return f"Withdrawal successful. Remaining balance is {self.bal}"
            
    def check_balance(self):
        print(f"Your current balance is: {self.bal}")
    
    def update_details(self, new_name, new_add):
        self.a_h_n = new_name
        self.add = new_add
        print("New name and address details updated successfully.")
        print("\n")
        
    def display_details(self):
        print("Account Holder Name:", self.a_h_n)
        print("Account Number:", self.a_n)
        print("Address:", self.add)
        print("Balance:", self.bal)

l= Bank_account("kavi",52154555," near govt hr sec school",8545.001)   
l.display_details()
print("\n")

result = l.withdraw(10000000) 
print(result)  
print("\n")

l.update_details("dinesh", "pallikaranai, chennai")
l.display_details()

l.check_balance()  

l.deposit(10000)



"""6.  Define a Matrix class of dimensions m X n (the values for m and n can be taken as input).
 Demonstrate matrix addition, subtraction, multiplication, element-by-element multiplication, 
scalar multiplication (use map here). Use operator overloading wherever possible.
 (Hint: In the constructor, use 'random' and create list of list using list comprehension. 
  In the arguments of constructor, send the number of rows and columns)
Ensure that your implementation follows best practices for class design and encapsulation in Python. 
Comment your code to explain the functionality of each method."""


        
import random

class Matrix:
    def __init__(self, m, n): 
        # sending number of rows and columns inside the constructor
        self.m = m
        self.n = n
        self.data = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            print("Matrices must have the same dimensions for addition.")
            return None
        result = Matrix(self.m, self.n)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.n)] for i in range(self.m)]
        return result

    def __sub__(self, other):
        if self.m != other.m or self.n != other.n:
            print("Matrices must have the same dimensions for subtraction.")
            return None
        result = Matrix(self.m, self.n)
        result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.n)] for i in range(self.m)]
        return result

    def __mul__(self, other):
        if self.n != other.m:
            print("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
            return None
        result = Matrix(self.m, other.n)
        result.data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.n)) for j in range(other.n)] for i in range(self.m)]
        return result

    def elementwise_multiply(self, other):
        if self.m != other.m or self.n != other.n:
            print("Matrices must have the same dimensions for element-wise multiplication.")
            return None
        result = Matrix(self.m, self.n)
        result.data = [[self.data[i][j] * other.data[i][j] for j in range(self.n)] for i in range(self.m)]
        return result

    def scalar_multiply(self, scalar):
        result = Matrix(self.m, self.n)
        result.data = list(map(lambda row: list(map(lambda x: scalar * x, row)), self.data))
        return result


# Example usage:
m1 = Matrix(2, 3)
m2 = Matrix(2, 3)
print("Matrix 1:")
print(m1)
print("Matrix 2:")
print(m2)

print("Matrix Addition:")
print(m1 + m2)

print("Matrix Subtraction:")
print(m1 - m2)

print("Matrix Multiplication:")
m3 = Matrix(3, 2)
print(m1 * m3)

print("Element-wise Multiplication:")
print(m1.elementwise_multiply(m2))

print("Scalar Multiplication:")
print(m1.scalar_multiply(2))




"""7. Create a Python class named Time that represents a moment of time. The class should have attributes hour, minute, and second. Include the following features:
    A constructor that initializes hour, minute, and second, with validation to ensure each attribute is within its correct range (hours: 0-23, minutes: 0-59, seconds: 0-59).
    A __str__() method that returns the time in a format hh:mm:ss.
    Methods set_time(hour, minute, second) and get_time() to update and access the time, respectively.
    An add_seconds(seconds) method that adds a given number of seconds to the current time object, adjusting the hour, minute, and second attributes accordingly.
"""
class Time():
    def __init__(self,hour, minute, second):
        self.set_time(hour, minute,second)
    
    def set_time(self, hour, minute, second):
        if 0<= hour <24 and 0<=minute<60 and 0<=second<60:
            self.hour=hour
            self.minute=minute
            self.second=second
        
        else:
            print("Time provided is not in the range")
        
        
    def __str__(self):
        if self.hour:
            return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        

    
    def get_time(self):
        return self.hour, self.minute, self.second
    
    def add_seconds(self, addseconds):
        self.second += addseconds
        if self.second >= 60:
            self.minute += self.second // 60
            self.second %= 60
        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute %= 60
        if self.hour >= 24:
            self.hour %= 24



# ob= Time(15,48,12)

# print(ob)

# ob.add_seconds(48)
# print(ob.get_time())

# ob.add_seconds(660)
# print(ob.get_time())


# print(ob)

ob2=Time(78,56,25)
ob2.set_time(78,56,25)

"""8.  Create a class named Geometry that provides static methods for various geometric calculations, such as area and perimeter, for different shapes (circle, rectangle, square). Include:
Static methods like circle_area(radius), rectangle_area(length, width), and square_area(side).
Static methods for perimeter calculations for the above shapes.
Ensure that methods check for valid inputs (e.g., positive numbers).
"""        
import math

class Geometry:
    @staticmethod
    def circle_area(radius):
        if radius > 0:
            return math.pi * radius ** 2
        else:
           return("Radius must be a positive number.")

    @staticmethod
    def circle_perimeter(radius):
        if radius > 0:
            return 2 * math.pi * radius
        else:
           return("Radius must be a positive number.")

    @staticmethod
    def rectangle_area(length, width):
        if length > 0 and width > 0:
            return length * width
        else:
           return("Length and width must be positive numbers.")

    @staticmethod
    def rectangle_perimeter(length, width):
        if length > 0 and width > 0:
            return 2 * (length + width)
        else:
           return("Length and width must be positive numbers.")

    @staticmethod
    def square_area(side):
        if side > 0:
            return side ** 2
        else:
           return("Side length must be a positive number.")

    @staticmethod
    def square_perimeter(side):
        if side > 0:
            return 4 * side
        else:
           return("Side length must be a positive number.")


# Example usage:
print("Circle area:", Geometry.circle_area(5))
print("Circle perimeter:", Geometry.circle_perimeter(-5))
print("Rectangle area:", Geometry.rectangle_area(3, 4))
print("Rectangle perimeter:", Geometry.rectangle_perimeter(3, 4))
print("Square area:", Geometry.square_area(5))
print("Square perimeter:", Geometry.square_perimeter(5))





















