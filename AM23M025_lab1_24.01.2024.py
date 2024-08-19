# 1.  WAP(Write a program) to find (print) the value of the following:

# 7*ln(3)*[ln(5)+ln(e^3)]

import math
print(float(7*math.log(3)*(math.log(5)+math.log(math.exp(3)))))
area_1= math.pi*(3/2)**2
area_2= math.pi*(5/2)**2
print(area_2-area_1)

# 2WAP to return the count of odd numbers and even numbers between 
# 7 and 80 (both inclusive) using arithmetic operators (without using loops) 
# and print it using ‘format strings’ in a single line. (
#  Refer to the attached file L3_output.py for examples of using formatted strings)



even=0
odd=0
i=0
def even_odd(lst):
    global even
    global odd
    global i
    if lst[i]%2==0:
        even+=1
    else:
        odd+=1
    if i in range(len(lst)-1):
        i+=1
        even_odd(lst)
    else:
        print(f"No of odd numbers {odd} and number of even numbers {even}")
    
my_list=list(range(7,81))
even_odd(my_list)

# 3. What are the different kinds of data types in python? Name them and explain their significance.WAP to demonstrate them in
# Python and print the size and type of each of them in ascending order.

""" Different kinds of data types:
    Integers- integer type 
    float- integer type 
    Strings- character type 
    Lists- mutable 
    tuple - immutable
    Dictionaries- mapping type 
    boolean type- true or false
       
    """


import sys

# Define variables
integer_var = 42
float_var = 3.14
string_var = "Hello, Python!"
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
set_var = {1, 2, 3}

# Calculate sizes
sizes = [
    (sys.getsizeof(integer_var), 'integer_var'),
    (sys.getsizeof(float_var), 'float_var'),
    (sys.getsizeof(string_var), 'string_var'),
    (sys.getsizeof(list_var), 'list_var'),
    (sys.getsizeof(tuple_var), 'tuple_var'),
    (sys.getsizeof(set_var), 'set_var')
]

# Sort by size
sizes.sort()
print(sizes)

# Print in ascending order of size
for size, name in sizes:
    print(f"{name}: Type: {type(eval(name))}, Size: {size} bytes")



# 4.  WAP to find the surface area of a cuboid with sides a,b,c. The values of a, b, c  should be random numbers generated between 10
# and 100. Take the seed value as user input. (use ‘random’ module).



import random

seed_value = 42
random.seed(seed_value)

a= random.uniform(10,100)
b= random.uniform(10,100)
c= random.uniform(10,100)

sur_area= 2 * (a*b+b*c+c*a)
print(sur_area)

#5. WAP to solve the quadratic equation of the form ax^2+bx+c=0, where a, b and c are real numbers and a ≠ 0 (Take a, b and c as user
#input).

import cmath


a= float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))


discriminant = b**2 - 4*a*c

if discriminant > 0 or discriminant<0 :
    # Two real and distinct roots or complex roots 
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
   
    root = -b / (2*a)
    print("Root:", root)



# 6. WAP to demonstrate various arithmetic operations by taking the two input numbers in a single line as space-separated-values (Use
# split function)

def add():
    return a+b
def subtract():
    return a-b
def multiply():
    return a*b
def divide():
    if b==0:
        return "cannot be divided by zero"
    return a/b


a,b= map(int,(input("enter two numbers").split(' ')))

print(f"addition:{add()},\n subtraction:{subtract()},\n multiplication:{multiply()},\n division:{divide()}")






# 7. Given the words ‘Learning’, ‘python’, ‘is’, ‘fun’. Accomplish the following tasks:
# a.    Create a sentence by combining these words : “Learning python is fun.” use(‘.join’)
# b.    Print the sentence “Learning datascience is fun.” (use ‘.replace’)
# c.    Generate an uppercase version of the sentence: “LEARNING PYTHON IS FUN.”
# d.    Rearrange the words to form a new sentence: “fun is python learning.”
# e.    Reverse each word in the sentence and print the result: “nuf si nohtyp gninrael.”

list1=['Learning','python','is','fun']
combined= " ".join(list1)
print(combined)
replacing= combined.replace('python','datascience')
print(replacing)
uppercase=combined.upper()
print(uppercase)
reversing=" ".join(list1[::-1])
print(reversing)
print(combined[::-1])
print("".join(reversed(combined)))

# 8. How object oriented programming in Python is different from other object oriented languages?

""" Answer: Dynamic assining of data to the data type without actually declaring it.(the data type is assigned while run time)
            python is better readable when compared to others.
            python has automatic memory allocation when compared to other languages( manual memory allocation )
            python comes with rich standard libraries for data science and data analytics(packages)
            python uses class inheritance and polymorphism which allows us to use code efficiently without repeating it.
            Dynamically typed allowing variables to change types at run time.
            python supports metaprogramming and reflection, enabling code to inspect and modify itself during runtime. This can be useful for building dynamic and extensible systems.
"""            

# 9.What are ‘built-in-functions’ in Python? Explain any five

""" Answer: Built in functions are default functions that comes directly with python (in built), enabling us to use it without any declarations.
            len()- returns the length of the list
            abs()- gives the absolute value of the decimal number
            sum()- returns the sum of the number in a particular list
            max() and min()- gives the maximum and minimum in a list
            type()- gives the type of the object whether it is a integer or float or string or dictionary."""
            
            
# 10.  WAP to:
# 1. Count the number of vowels in a given string.
# 2. Check if a given string is palindrome.
ing = 0

def counting(lst):
    global ing
    for char in lst:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            ing += 1

string = "My name is Kaviyarasan"
counting(string)

print("Number of vowels", ing)


list1="amma"
if list1[::]==list1[::-1]:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")





            
            


            

