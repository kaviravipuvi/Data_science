# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:06:03 2024

@author: Kaviyarasan PR
"""



"""1.Write a program (WAP) to implement the following operations on a collection of library books:

(a) Construct a catalog of books, with each book having an author's name, book title, ISBN number, publication year, and number of pages.

(b) Add a new book to the catalog, ensuring that the books are kept in ascending order based on the publication year.

(c) Locate a book by its ISBN number and delete the book's entry from the catalog.

(d) Insert a new book entry at the end of the catalog using the provided book information.

(e) Identify and remove any duplicate entries in the catalog, preserving only one copy of each book based on its ISBN number.

(f) Reorganize the entire catalog so that the books are sorted in descending order by the number of pages.
""" 
catalog = []

# Construct a catalog
book1 = {"author": "kavi", "title": "discipline", "isbn": "123456789", "publication_year": 2000, "num_pages": 200}
book2 = {"author": "dinesh", "title": "hardwork", "isbn": "234567890", "publication_year": 1990, "num_pages": 300}
book3 = {"author": "rohit", "title": "consistency", "isbn": "345678901", "publication_year": 2010, "num_pages": 150}

if not catalog:
    catalog.append(book1)
else:
    for i, b in enumerate(catalog):        
        if book1["publication_year"] < b["publication_year"]:
            catalog.insert(i, book1)
            break
    else:
        catalog.append(book1)

if not catalog:
    catalog.append(book2)
else:
    for i, b in enumerate(catalog):
        if book2["publication_year"] < b["publication_year"]:
            catalog.insert(i, book2)
            break
    else:
        catalog.append(book2)

if not catalog:
    catalog.append(book3)
else:
    for i, b in enumerate(catalog):
        if book3["publication_year"] < b["publication_year"]:
            catalog.insert(i, book3)
            break
    else:
        catalog.append(book3)
print("sorting based on th publication year")        
print(catalog)
print("\n")


print("Adding a new book")
new_book = {"author": "athul", "title": "forrest_gump", "isbn": "456789012", "publication_year": 2020, "num_pages": 250}
if not catalog:
    catalog.append(new_book)
else:
    for i, b in enumerate(catalog):
        if new_book["publication_year"] < b["publication_year"]:
            catalog.insert(i, new_book)
            break
    else:
        catalog.append(new_book)

print(catalog)
print("\n")

print("Locate and delete a book")

isbn_to_delete = "234567890"
for i, book in enumerate(catalog):
    if book["isbn"] == isbn_to_delete:
        del catalog[i]
        break


print(catalog)
print("\n")

print("Inserting a new book entry at the end")
new_book_at_end = {"author": "sushant", "title": "atomic habits", "isbn": "567890123", "publication_year": 2005, "num_pages": 180}
catalog.append(new_book_at_end)

print(catalog)
print("\n")

print("Remove duplicates")
seen_isbns = set()
unique_catalog = []
for book in catalog:
    if book["isbn"] not in seen_isbns:
        unique_catalog.append(book)
        seen_isbns.add(book["isbn"])
catalog = unique_catalog

print(catalog)
print("\n")

print("Reorganizing based on the number of pages")
for i in range(len(catalog)):
    for j in range(i + 1, len(catalog)):
        if catalog[i]["num_pages"] < catalog[j]["num_pages"]:
            catalog[i], catalog[j] = catalog[j], catalog[i]

print(catalog)
print("\n")

"""2. Write a program using list comprehension

a) To add the corresponding elements of two lists and print the new list.

b) To perform element wise multiplication of two lists and print the new list.

c) To create a list of the unique characters of a given string. 

Eg: input = “hello” , output = [‘h’, ‘e’, ‘l’, ‘o’]"""

li1=[1,2,9,6,78]
li2=[223,3,1,4,5]

li_add=[li1[i]+li2[i] for i in range(0,5)]
print(li_add)

li_mul= [li1[i]*li2[i] for i in range(0,5)]
print(li_mul)

given_string = "kaviyarasan"
unique_string = []

for char in given_string:
    if char not in unique_string:
        unique_string.append(char)        
print(unique_string)


"""3. Using the zip function, WAP

a) To add the elements of 2 matrices (Define matrices as per your wish).

b) To perform element wise multiplication on 2 matrices.
"""

m1=[[1,8,6],[4,8,98],[98,65,78]]
m2=[[556,87,54],[98,54,75],[87,65,25]]
add=[]
mul=[]
for r1,r2 in zip(m1, m2):
    print(r1)
    print(r2)
    
    for x,y in zip(r1,r2):
        print(x)
        print(y)
        add.append(x+y)
        
print(add)

for r1,r2 in zip(m1, m2):
    print(r1,r2)
    for x,y in zip(r1,r2):
        mul.append(x*y)
        
print(mul)


""" 4. List of List : Given a square matrix represented as a list of lists, 

a) WAP to print the row sum, column sum and trace of the matrix 

b) WAP to print the transpose of the matrix.

c) WAP to check whether the given matrix is symmetric or not.

d) WAP to check whether the Identity matrix (I) is positive definite or not by using Quadratic form method (x^T*I*x > 0), where x is any non zero vector.
"""

rowsum=0
for row in m1:
    print(sum(row))

   
for row in m2:
    print(sum(row))

transposed_matrix = list(zip(*m1))
print(transposed_matrix)

column_sum=0
for column in transposed_matrix:
    column_sum=sum(column)
    print(column_sum)

if len(row)==len(list(column)):
    print("symmetric matrix")
else:
    print("non symmetric matrix")





def is_positive_definite_identity_matrix(I):
    n = len(I)
    x = [1] * n  # We choose a vector of ones for simplicity
    print(x)
    quadratic_form = sum(x[i] * I[i][j] * x[j] for i in range(n) for j in range(n))
    print(quadratic_form)
    return quadratic_form > 0

# Example: Identity matrix (I)
identity_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Check if the identity matrix is positive definite
if is_positive_definite_identity_matrix(identity_matrix):
    print("The Identity matrix is positive definite.")
else:
    print("The Identity matrix is not positive definite.")



"""5.  List of Lists : WAP to remove sub lists from a given list of lists that contain an element outside a given range.

Example :

Input : [[3], [1, 3, 2], [0, 1, 9, 3, 5, 7], [9, 10], [13, 14, 16, 17]]  Range: 1, 5

Output : [[3], [1, 3, 2]]

Explanation : If a sublist has a number that is other than 1, 2, 3, 4, 5, remove the sublist from the list of lists and print the remaining sublists as a lists of lists

"""

inp= [[3], [1, 3, 2], [0, 1, 9, 3, 5, 7], [9, 10], [13, 14, 16, 17]]
new=[]
for _ in inp: 
    sublist=True
    for ele in _:
        if not 1<=ele<=5:
            sublist=False
            break
    if sublist:
        new.append(_)   
            
print(new)


