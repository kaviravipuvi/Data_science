"""tuples"""

tup=()
print(tup)
print(type(tup))

tup1=(10)
print(tup1)
print(type(tup1))

tup1=(10,)
print(tup1)
print(type(tup1))



tup3= (9,9,10,1,3,5,9)
print(tup3[0])
    
print(tup3[::-1])
tup4=()
tup4= sorted(tup3)
print(tup4)

print(len(tup3))

lst=list(tup3)
print(lst)

string="kaviyarasan"
for char in string:
    a=tuple(char)
    print(a)
    
tup4= tuple(string)
print(tup4)

tup5=([1,2,3,4,5],7,5,2,4,1)
print(max(tup5[0]))


tup5=(1,2,3,4,5,7,5,2,4,1)

tup6=(9,7,294,37234,tup5,892,75)

print(tup6)
print(max(tup5))

for num in tup5:
    print(num)

print(sum(tup5))

tup_comp = tuple([(x**2, x**3) for x in range(5)])
print(tup_comp)
print(*tup_comp)

tup2=tuple([num for num in range(1,10)])
print(tup2) 

tup2=tuple([[num] for num in range(1,10)])
print(tup2)

print(tup5.count(7))

tup6=tup5+tup1
print(tup6)


names=('ram','raja','geetha')
gender=('male','male','female')
print(len(names))
for i in range(len(names)):
    tup7=tuple([names[i]+ " "+gender[i]])
    print(tup7)
    

names = ('Ram', 'Raja', 'Geetha', 'Ramya')
gender = ('male', 'male', 'female', 'female')

grouped_tuples = tuple(zip(names, gender))
print(grouped_tuples)
