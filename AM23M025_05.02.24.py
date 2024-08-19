# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:06:18 2024

@author: Kaviyarasan PR
"""
"""TOPIC:tuple matrix and containers """
mat=[[1,2,3],[4,5,6],[7,8,9]]
for i in zip(mat[0],mat[1]):
    print(i)
    print(sum(i))
    
ite = zip(*mat)
print(ite)
lst = list(ite)
print('Matrix inverse = ', lst)

setk= {10, 20, 30, 40, 50}
setd={41,84,21,85,47}
print(type(setk))


for s in setk:
    print(s)
    
sorted_setk = sorted(setk)
print(sorted_setk)
print(max(setk))
print(set(sorted_setk))

setk.add(90)
print(setk)

setk.remove(100)
print(setk)

""" if the element is not present in the set then remove throws errors whereas discard doesn't throw error"""

setk.discard(100)
print(setk)

setk.clear()
print(setk)


"""hash table and dictionary are closely related
    set elements have to be unique
    set is unordered cannot be indexed and sliced"""
    
    
'''HW: frozenset()'''

setA = frozenset({10, 20, 30})
setB = frozenset({40, 50, 60})
fr_sos = {setA, setB}
print(fr_sos)

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

setC = set()
setC.add(tup1)
print(setC)
setC.add(tup2)
print(setC)



update_set= setk.update(setd)
print(update_set)

superset= setk.issuperset(setd)
print(superset)

subset= setd.issubset(setk)
print(subset)

disjoint=setd.isdisjoint(setk)
print(disjoint)

"""embedding and unpacking"""
seta={20,25,31,*setk}
print(seta)

"""set are mutable using member functions such as update functions"""

"""set comprehension"""

setn=set()
for _ in range(0,101):
    setn.add(_)
print(setn)

setm={x**2 for x in range(100)}
print(setm)




