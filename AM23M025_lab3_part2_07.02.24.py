# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:11:04 2024

@author: Kaviyarasan PR
"""

"""6. List comprehension  : Given two lists of equal length, list1 contains the integers and list2 contains alphabets. Using list comprehension, WAP

a) To generate a list containing the squares of elements from list1.

b) To generate a list containing pairwise corresponding elements in the form of tuple.

c) To generate a list containing all possible combinations of elements from the two lists.

d) To generate a list containing elements of list1 and list2 alternatively.
"""

li3=[4,5,8,7,3]
li4=['a','b','c','d','e']

square=[li3[i]*li3[i] for i in range(len(li3))]
print(square)

pairwise=[tuple(str(li3[i])+li4[i])for i in range(len(li3))]
print(pairwise)


combinations = [str(li3[i]) + li4[j] for i in range(len(li3)) for j in range(len(li4))]
print(combinations)


alternate=[item for sublist in zip(li3, li4) for item in sublist]

print(alternate)


"""8. Write a code snippet in Python that takes a string as input and returns a tuple of tuples. Each inner tuple should contain a character from the input string and its corresponding ASCII value.

Sample example: Input_string = "Design",  Output_tuple = (('D', 68), ('e', 101), ('s', 115), ('i', 105), ('g', 103),('n', 110) )
"""
y=[]
name= "Kaviyarasan"
for char in name:
     y.append((char,ord(char)))
print(tuple(y))

"""9. Create a program that takes a list of tuples containing student name and roll number and returns a new list of tuples containing only those tuples whose first element is a vowel (a, e, i, o, u, A, E, I, O, U).

Sample example: list_of_tuples = [("aditi", 1), ("tanya", 2)], Output_list_of_tuples = [("aditi", 1)]
"""


list_of_tuples = [("Ellona", 1), ("abi", 2), ("ernest", 3), ("kavi", 4)]
vowels =  set("aeiouAEIOU")

output_list_of_tuples = []

for name, roll in (list_of_tuples):
    if name[0] in vowels:
        output_list_of_tuples.append((name, roll))

print(output_list_of_tuples)

"""10.  Create a set of all numbers between 1 and 20 that are either divisible by 3 or 5, using set comprehension.
"""
list5=[i for i in range(1,20) if i%5==0 and i%3==0]
print(list5)