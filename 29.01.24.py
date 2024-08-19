
""" list containers"""


lst= [100]*5
print(lst)

list1=['kavi', 100,90.008, 'dinesh','python']
print(list1[3])

for ele in list1:
    print(ele)
    print(type(list1))

list1[0]=900
print(list1[:2:-1])
print(list1[2:2:])

""" array vs list in memory allocation :HW """

list2= ['kavi','dinesh']
print(len(list2[1]))
print(len(list2[0]))
count=0
for words in list2:
    for letters in words:
        count+=1
        
print(count)

list3= lst+list1
print(list3)

""" diff bw count and len"""
sample = [2, 10, 1, 1, 5, 2]
print(len(sample))
print(sample.count(1))


list3[:]= []
print(list3)



""" member function vs built in fn vs library funciton"""

vow_lst = ['o', 'a', 'e', 'i', 'u']
print(sorted(vow_lst))


print(list('Kaviyarasan'))
print(max(list('Kaviyarasan')))
print(min(list('Kaviyarasan')))

print(list('Raman')) 
print(max(list('Raman')))
print(min(list('Raman')))
print(sorted(list('Raman')))
print(len(list('Raman')))

lst5 = []
if not lst5:
    print('True')
    print(lst5)


marks=[80,90,100,12,90,100]
print(max(marks))
print(min(marks))
total=0
for mark in marks:
    total+=mark
average= total/len(marks)
print(average)




lst = [10, 30, 20, 15, 20, 60, 80, 70]

print('Printing the list', lst)

lst.append(23)

print('appending', lst)

lst.pop()

print(' pop()', lst)

lst.pop(3)

print( 'after popping 4th element', lst)

lst.sort()

print('sorting', lst)

lst.remove(20)

lst.insert(3, 34)   

print(' after insertion', lst)

print('number of occurances of 20: ',lst.count(20))

print('index of number 20: ', lst.index(10))

lst.sort(reverse=True)

print('after sorting', lst)

lst.reverse()

print(' sorting in reverse', lst)


"""Shallow copy and deep copy"""

import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
print ("The original elements before deep copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")
li2[2][0] = 7
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
	print (li2[i],end=" ")

print("\r")
print ("The original elements after deep copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")
    
    
import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")
li2[2][0] = 7
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")

kavi=[i for i in range(21)]
print(kavi)
kavi.sort(reverse=True)
print(kavi)
for _ in range(21):
    kavi.pop()
    print(kavi)


j=[]
j.append(100)
print(j) 