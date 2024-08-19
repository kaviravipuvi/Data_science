# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:50:54 2024

@author: Kaviyarasan PR
"""


employees = {
    101: {'name': 'Alice', 'salary': 50000, 'experience': 3},
    102: {'name': 'Bob', 'salary': 60000, 'experience': 5},
    103: {'name': 'Charlie', 'salary': 45000, 'experience': 2}
}

sort= dict(sorted(employees.items(), key=lambda item: item[1]['salary']))


print(sort)
for emp_id, emp_info in sort.items():
    print(f"{emp_id},{emp_info['name']}, {emp_info['salary']},{emp_info['experience']}")

new_employee = {'name': 'David', 'salary': 55000, 'experience': 4}
employees[104] = new_employee

print(employees)

sort= dict(sorted(employees.items(), key=lambda item: item[1]['salary']))

for iid , info in sort.items():
    print(iid, info['name'],info['salary'], info['experience'])


"""7. You are given two Python dictionaries,
 A and B, with keys as alphabets and values as random integers. Write a Python function to create a third dictionary C, that combines A and B. For common keys, 
the value in C should be the sum of values from A and B. """

A= {'a':3, 'b':5,'c':7}
B={'a':3, 'b':7, 'c':11,'d':6}

C={}

for key1, value1 in A.items():
    if key1 in B.keys():
        C[key1]=value1+B[key1]

for key2, value2 in B.items():
    if key2 not in A.keys():
        C[key2]=value2

print(C)


""" 8. Assume you have a list of lists, where each inner list contains two elements:
    a key and a value. Write a Python function that takes the list of lists as input and returns a list of dictionaries, 
    where each dictionary contains a key-value pair from the original input list.

"""
def list_dict(list_in_list):
    dicti=[]
    for inner in list_in_list:
        dicti.append({inner[0]:inner[1]})
    return dicti


i = [['kavi', 'hakuna matata'], ['dinesh', 'atomic habits'], ['srihari', 'venkat']]
out= list_dict(i)
print(out)

"""9. Illustrate the usage of positional and keyword arguments using suitable examples."""

""" positional arguments are passed into the function based on the position but keyword arguments
    it's like a key value pair irrespective of the position and order it funcitons the same."""

def pos_and_key(name, roll):
    return name, roll


print(pos_and_key("name:" "kaviyarasan", "rollno:" "am23m025"))  

print(pos_and_key("name:" "am23m025", "rollno:" "kaviyarasan"))  

print(pos_and_key(name="kaviyarasan", roll="am23m025"))

print(pos_and_key(roll="am23m025",name="kaviyarasan"))


""" 10. Write a function to find the maximum of n numbers using variable length positional arguments """


def maximum(*args):
    if len(args)==0:
        return "No input provided"
    else:
        return max(args)
inp=(200,100,400,600,700,20000,50,10,45660215,8871614589)
print(maximum(*inp))





"""11. Write a function to concatenate n strings using variable length keyword arguments."""


def concatenate(**kwargs):
    concat=''
    for key, value in kwargs.items():
        concat+=value
    return concat

print(concatenate(inp='kavi',inp1='dinesh',inp2='arun'))










