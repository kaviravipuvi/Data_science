# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:01:32 2024

@author: Kaviyarasan PR
"""

"""1. Explore the use and syntax of common built-in functions: 

range(), 

iter(), 

eval(), 

enumerate(), 

zip(), 

lambda, 

input(), 

map(), 

filter(), 

next()

reduce()

Include a short description and a practical code example for each, ensuring clarity through comments."""

dic={"kavi":1, "arun":11, "dinesh":120}

print(range(len(dic)))


"""cannot pass dictionary directly on to the range since it expects an integer"""

iterator= iter(dic)
for key in iterator:
    print(key)
    print(dic[key])
    
    """iter sets the dictionary for iterations so that we can use next inbuilt function to iterate through"""

kaviyarasan= "hello world"
x = 'print(kaviyarasan)'
eval(x)

for index, (key, value) in enumerate(dic.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")
    
    """using enumerate to extract the key and values of the dictionary so that we can access each of them seperately"""

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd':-5}
dict2 = {'x': 10, 'y': 20, 'z': 30}


keys_zip = zip(dict1.keys(), dict2.keys())
for item in keys_zip:
    print(item)
keys_values = zip(dict1.values(), dict2.values())   
for item in keys_values:
    print(item)
keys_items = zip(dict1.items(), dict2.items())   
for item in keys_items:
    print(item, end=" ")
    
""" using zip function to access the keys , values and items in a dictionary, basically it merges the two dictionary based on the user convinience"""


doubled_dict = {key: (lambda x: x * 2)(value) for key, value in dict1.items()}
print(doubled_dict)

"""lambda can have many number of arguments, but it can have only one expression"""

mapped= map(lambda value: value*2, dict1.values())
print(dict(zip(dict1.keys(), mapped)))

"""map function is used to map the values to the corresponding keys"""

filtered = filter(lambda value: value >= 1, dict1.values())
filtered_values = list(filtered)
print(filtered_values)
print({key: value for key,value in dict1.items() if value in filtered_values})

"""filter is used to filter some of the values in the dictionary that may be based on the values, keys or items and then we need to store the filtered """
""" one in the list or else the filtered list will be vanished from the system memory"""


next_key = next(iter(dict1))
print(next_key)  
next_value = dict1[next_key]
print(next_value)  
""" next to iterate over the next key or next values"""


from functools import reduce


# Using reduce to compute the sum of values in the dictionary
total_sum = reduce(lambda x, key: x + dict1[key],dict1, 0)
print(total_sum) 

total_mul= reduce(lambda x, key: x * dict1[key],dict1, 1)
print(total_mul) 

"""using reduce function to simplify the operation of sum, multiplication, subtraction or others, by setting a initial value to the variable """




"""Write a Python function that sorts a dictionary based on the length of values.

Sample:

Input: {'lemon':'yellow','apple':'red'} output: {'apple':'red','lemon':'yellow'}"""


input_dict = {'lemon': 'yellow', 'apple': 'red','watermelon':'orange','grape':'purple'}


sorted_dict = dict(sorted(input_dict.items(), key=lambda x: len(x[1])))

print(sorted_dict)


"""3. Develop a Python program that executes the following tasks with a user-provided string:

a. Prompt the user to input a string.

b. Create a dictionary from the string where each key is a unique alphabet character and the corresponding value is the frequency of that character's occurrence in the string.

c. Generate a sorted list of tuples from the dictionary based on character frequency (values).

d. Generate a sorted list of tuples from the dictionary based on the alphabet characters (keys).

e. Identify the three most frequently occurring characters. In the event of a frequency tie, prioritize characters in lexicographical order.

Your program should showcase proficiency in dictionary operations, sorting mechanisms, and handling of ties in frequency counts. Comment your code to outline the process and decisions made.

sample:

input = 'GOOGLE'

Here, the most repeated characters are G:2, O:2. But, L,E are occurring only a single time which is tied for the third position here, so here we take E as it comes first in the lexicographical order.

"""


input_string = input("Enter a string: ")

char_freq = {}


for char in input_string:
    if char.isalpha():
        char_freq[char] = char_freq.get(char, 0) + 1




sorted_by_freq = sorted(char_freq.items(), key=lambda x: x[1])


sorted_by_char = sorted(char_freq.items())

most_frequent = sorted_by_freq[:3:-1]

most_frequent.sort(key=lambda x: x[0])


print(char_freq)
print(sorted_by_freq)
print(sorted_by_char)
print(most_frequent)

"""4. Write a function called lookup_student that takes a dictionary representing student records, where names are keys and roll numbers are values. The function should search for a specified student name and return the corresponding roll number if found; otherwise, it should return "Not Found" 

Example:

records = { "Alice" : "AB111", "Bob" : "EE200", "David" : "XY333"}

print(lookup_student(records, "Bob")) : Should print "EE200"

print(lookup_student(records, "John")) : Should print "Not Found"
"""

def lookup_student(records, x):    
    if x in records:        
        return records[x]
    else:
        return "Not Found"


records = { "Alice" : "AB111", "Bob" : "EE200", "David" : "XY333"}
print(f"Roll number is: {lookup_student(records, 'David')}")
print(f"Roll number is: {lookup_student(records, 'John')}")



"""5. Given a list of integers, write a Python program to:

a) Find the frequency of each integer in the list and store the result in a dictionary.

b) Print the maximum integer and its frequency.

c) Remove duplicates from the list and print the new list without changing the order of elements. Do this operation without using the set data type.

d) Remove duplicates from the list and print the new list. Do this operation using the set data type.

"""

numbers = [45,85,77,65,77,10,54,10,54,16,55,4,88,77,22,100]

freq_dict = {}
for num in numbers:
   value = numbers.count(num)
   freq_dict[num] = value
print(freq_dict)
   

max_num =max(numbers)
print(max_num)
print(freq_dict[max_num])



unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
        
print(unique_list)

print(list(set(numbers)))



