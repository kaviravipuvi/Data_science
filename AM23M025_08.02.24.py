# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:09:37 2024

@author: Kaviyarasan PR
"""

A={10,25,50,60,70,20}
B={20}

A|=B
print(A)


A={10,25,50,60,70,20}
B={20}

A&=B
print(A)


A={10,25,50,60,70,20}
B={20}

A-=B
print(A)

A={10,25,50,60,70,20}
B={20}

B-=A
print(B)

A={10,25,50,60,70,20}
B={20}

A^=B
print(A)



dct1 = {"10" : 100, "20" : 200, "ED1" : "name1", "ED2" : "name2"}

print(dct1["10"])


"""keys have to be unique but values need not to be unique and values can be repeated by using different unique keys"""

dct1 = {"10" : 100, "20" : 200, "10" : "name1", "ED2" : "name2"}4
print(dct1["10"])

studlist = {'Anand' : {'DOB' : '20/11/2001', 'Roll' : 'ED1234' },
'Ramesh' : {'DOB' : '19/11/2001', 'Roll' : 'ED1235' },
'Kamesh' : {'DOB' : '21/11/2001', 'Roll' : 'ED1236' } }
''
# print('printing the nested list', studlist)

for k in studlist.keys():
    print(k)
    print(studlist.keys())
    print(k, studlist[k])
    
dct1 = {20 : 100, 10 : 200, 'ED2' : 'name1', 'ED1' : 'name2'} 

print (dct1)

print(dct1[10], dct1['ED1'])

print('\n')
print('Using Iterator over key-value pairs');
for k, v in dct1.items():
    print(dct1.items())
    print(k, v)
    
    
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_list = sorted(my_dict.items())
print(sorted_list)

sorted_dict = {}
for key, value in sorted_list:
    sorted_dict[key] = value

print(sorted_dict)

new = dict()
new.update(dct1)
new.update(my_dict)
print(new)

# new.clear()
print(new)

dct2={"70":100,"kavi":100, "ramesh":700}
newnew= dict()
newnew.update(dct2)
newnew.update(new)
print(newnew)

newnew.pop()
print(newnew)


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

concatenated_dict = {}
concatenated_dict.update(dict1)
concatenated_dict.update(dict2)
concatenated_dict.update(dict3)

print(concatenated_dict)

dict1.clear()
dict2.clear()
dict3.clear()
print(dict1)
print(dict2)
print(dict3)

print(not bool(dict1))
print(not bool(dict2))
print(not bool(dict3))















