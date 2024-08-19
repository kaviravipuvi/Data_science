
"""1. Write a program to print numbers divisible by both 7 and 8. Numbers between 1 and 1000.
[Numbers like 56, which are both divisible by 7 and 8]
a. Using continue statement
b. Using the pass statement"""

print("Numbers divisible by both 7 and 8 between 1 and 1000:")
for _ in range(1,1001):
    if _%7==0 and _%8==0:       
        print(_)
    else:
        pass

for _ in range(1, 1001):
    if _ % 7 != 0 or _ % 8 != 0:
        continue
    print(_)


"""2. Number 34567222541147 has been given. Print the addition of all even digits and the addition of all odd digits.
[Sample input = 156893, Sample Output: sum_even = 14 , sum_odd = 18]"""

number= "34567222541147"
even=0
odd=0
for digit in number:
    if int(digit)%2==0:
        even+=int(digit)
    else:
        odd+=int(digit)
print(odd)
print(even)


"""3. Describe conditional expression. Write a program to print the maximum and minimum numbers from a list using conditional expression. Use
the max () and min () functions to verify your output."""
import random
random.seed(42)
l=[random.randint(1,100) for _ in range(10)]
print(l)
x=0
y=100
for i in l:
    if i > x:
        x=i
print(f"maximum value:{x}")
print(f"maximum value:using max funciton:{max(l)}")

for i in l:
    if i < y:
        y=i
print(f"minimum:{y}")
print(f"minimum value:using min function:{min(l)}")


"""4. Pascal’s  Triangle : Print the following pattern for the given N number of rows"""
   
def print_pascals_triangle(n):
    for i in range(n):
        # Calculate the value of the elements in the current row
        num = 1
        for _ in range(n - i - 1):
            print(" ", end=" ")  # Print leading spaces for alignment
        for j in range(i + 1):
            print(num, end="   ")  # Adjust the spacing for alignment
            num = num * (i - j) // (j + 1)
        print()

# Define the number of rows for Pascal's triangle
num_rows = 8

# Print Pascal's triangle with spacing alignment
print_pascals_triangle(num_rows)
   
   
"""5. A palindrome sentence is a phrase or sentence that reads the same forward as it does backward, ignoring spaces, punctuation, and
capitalization.
A) Take a number as input, determine if it is a palindrome, considering only numeric characters. Eg: 2442
B) Now, take a string as an input and check whether it is Palindrome or not.  eg: "Was it a car or a cat I saw?"  
    The expected output for this example will print, 'True"""
    
lo=int(input("enter a number:"))
temp=lo
rev=0
while(lo>0):
    dig=lo%10
    rev=rev*10+dig
    print(rev)
    lo=lo//10
if(temp==rev):
    print("palindrome")
else:
    print("not a palindrome")    


s = "Was it a car or a cat I saw".lower()
s = ''.join(list(s))
s = s.replace(" ", "")  

print(s)

first = 0
last = len(s) - 1
is_palindrome = True

while first < last:
    if s[first] != s[last]:
        is_palindrome = False
        break
    first += 1
    last -= 1

if is_palindrome:
    print("True: it is a Palindrome")
else:
    print("False: it is not a palindrome")




"""6. Describe chr () and ord () functions. Write a small program to show its functionality.Using these functions,write a program to print:
Pattern for N=4
  A
  B B
  C C C
  D D D D"""

N=int(input("enter a number"))
first= ord('A')
for _ in range(N):
    print((chr(first+_)+" ")*(_+1))

"""7.You have a single list of names (each name should have first name and last name). Write a programme
(a) to print the first names.
(b) to print the last names.
(c) to print each name as 'last_name first_name.
(d) to print the names in the sorted order with respect to last name
Example :Input list: ['Mark Antony', 'Mohan Raj']"""


joe = ['kavi pr', 'Mohan Raj', 'Mark Antony']
f_n = []
l_n = []
lnfn = []

# Extract first and last names
for name in joe:
    first_name, last_name = name.split(" ")
    f_n.append(first_name)
    l_n.append(last_name)
    lnfn.append(last_name + " " + first_name)

print("First Names:", f_n)
print("Last Names:", l_n)
print("Last name and first name:", lnfn)

# Sort last names and rearrange first names accordingly
sorted_last_names = sorted(l_n)
sorted_first_names = [f_n[l_n.index(last_name)] + " " + last_name for last_name in sorted_last_names]

print("Sorted First Names based on Last Names:", sorted_first_names)



"""8. WAP to find the minimum of 3 numbers using
 a) with conditional expressions. (No loops should be used)
 b) with nested conditional expression. (No loops should be used)
 c) similar to problem (b), find the minimum of 4 numbers"""


a, b, c = 1000,100,56000

if(a < b and a < c):
	print(a, " A is the smallest")
elif(b < a and b < c):
	print(b, " B is the smallest")
else:
	print(c, "C is the smallest")


a, b, c = 1, 100, 5

if a < b:
    if a < c:
        print(a, "is the smallest")
    else:
        print(c, "is the smallest")
else:
    if b < c:
        print(b, "is the smallest")
    else:
        print(c, "is the smallest")



# Minimum of 4 numbers using nested conditional expressions
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

minimum = a if a < b else (b if b < c else (c if c < d else d))
print("Minimum of the four numbers is:", minimum)

"""9. Create a list of departments in IIT Madras (Minimum 5 ) and perform the following operations:
 append
remove pop
insert  reverse
sort
count
index
extend
slice
clear"""

departments = ["CSE", "EE", "Mechanical Engineering", "Civil", "Aerospace"]


departments.append("Chemical")
print(departments)

departments.remove("Civil")
print(departments)


popped_department = departments.pop()
print("Popped department:", popped_department)
print(departments)


departments.insert(1, "Biotechnology")
print(departments)

departments.reverse()
print(departments)

departments.sort()
print(departments)


count = departments.count("EE")
print(count)


index = departments.index("Mechanical Engineering")
print(index)


other_departments = ["Ocean Engineering", "Metallurgical and Materials Engineering"]
departments.extend(other_departments)
print(departments)


sliced_departments = departments[2:5]
print("Sliced departments:", sliced_departments)


departments.clear()
print("After clear:", departments)

        



















    
    
    
    
    
    
    
    