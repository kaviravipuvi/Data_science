""" Decision controls - if elif else"""
a,b= map(int, input("enter the two numbers: ").split(' '))
if a<b:
    print("a less than b")
else:
    print("b less than or equal to a")


item= int(input("enter the number of items:"))
if item<10:
    dis=100
elif item<20:
    dis=200
else:
    dis=500
print(f"number of items: {item} and the discount is {dis}")



a,b,c=5,100,900
print(a==b)

if a>b>c:
    print(" a is the largest")
elif b>c:
    print("b is the largest")
else: 
    print("c is the largest ")
    
    
maxi = a if a > b and a>c else c
print('max value of a and b using conditional expression is ', maxi)

print(a!=b!=c)

maxi = a if a > b else b

maxi1 = maxi  if maxi > c else c

print(maxi, maxi1)


a= not a
print(a)


a= not True
print(a)

i=0
while i<10:
   print("kavi and dinesh") 
   i+=1

for i in range(10):
    i+=2
    print("dinesh and kavi")
    
stri= "kaviyarasan"
for char in stri:
    print(char)

while i<10:
    for char in stri:
        print(char)
    i+=1
    if i==5:
        break

