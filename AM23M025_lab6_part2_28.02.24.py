# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:34:25 2024

@author: Kaviyarasan PR
"""

"""6.    Create a base class Vehicle with the following attributes:

         make (string)

         model (string)

         year (int)

       Create a method initialize_vehicle to set the above attributes. Also, create a method display_vehicle to print these attributes.

       Create a class Car inherited from Vehicle with the following additional attribute:

         fuel_type (string)

       Create a method get_car_details to initialize the above attribute along with Vehicle attributes.

       Also, create a method display_vehicle to print these attributes along with Vehicle attributes.

       Create a class Bike inherited from Vehicle with the following additional attribute:

           gear_count (int)

      Create a method get_bike_details to initialize the above attribute along with Vehicle attributes.

      Also, create a method display_vehicle to print these attributes along with Vehicle attributes.

      Create two different objects for Car and Bike and demonstrate each of the methods.

     Example -1:

         my_car = Car()

        my_car.get_car_details("Toyota", "Camry", 2020, "Petrol")

        my_car.display_vehicle()

        Output:

           Make: Toyota, Model: Camry, Year: 2020

           Fuel Type: Petrol

          Example -2 :

           my_bike = Bike()

           my_bike.get_bike_details("Yamaha", "YZF R1", 2021, 6)

           my_bike.display_vehicle()

          Output:

             Make: Yamaha, Model: YZF R1, Year: 2021

             Gear Count: 6
"""



class Vehicle:
    def __init__(self, make=None, model=None, year=None):
        self.initialize_vehicle(make, model, year)

    def initialize_vehicle(self, make=None, model=None, year=None):
        self.make = str(make)
        self.model = str(model)
        self.year = int(year) if year is not None else None

    def display_vehicle(self):
        print("Printing vehicle details\n")
        print(f"Make: {self.make} Model: {self.model} Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make=None, model=None, year=None, fuel_type=None):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        
    def get_car_details(self, make, model, year, fuel_type):
        self.initialize_vehicle(make, model, year)
        self.fuel_type = fuel_type
        
    def display_vehicle(self):
        super().display_vehicle()
        print(f"Fuel type: {self.fuel_type}")

# 
class Bike(Vehicle):
    def __init__(self, make=None, model=None, year=None, gear_count=None):
        super().__init__(make, model, year)
        self.gear_count = gear_count
        
    def get_bike_details(self, make, model, year, gear_count):
        self.initialize_vehicle(make, model, year)
        self.gear_count = gear_count
        
    def display_vehicle(self):
        super().display_vehicle()
        print(f"Gear Count: {self.gear_count}")


my_car = Car()
my_car.get_car_details("Toyota", "Camry", 2020, "Petrol")
my_car.display_vehicle()
        
my_bike = Bike()
my_bike.get_bike_details("Yamaha", "YZF R1", 2021, 6)
my_bike.display_vehicle()




"""

7. Suppose you are building a Python program to manage a school's student data. 
You need to create a Student class that contains information such as the student's name, age, grade, and class schedule. 
Additionally, there are some attributes that are shared by all students, such as the school name, the total number of students, 
and the number of classes offered.

How can you use class variables in Python to define these shared attributes of the Student class?
 What are the advantages of using class variables in this scenario?
 Can you provide an example program that demonstrates the use of class variables in the Student class? 

"""


class Student:
    # Class variables
    school_name = "Adharsh Vidhyalaya Matriculation School"
    total_students = 0
    total_classes_offered = 6

    def __init__(self, name, age, grade, gender, schedule):
        self.name = name
        self.age = age
        self.grade = grade
        self.gender= gender
        self.schedule = schedule
        # Increment total_students when a new instance is created
        Student.total_students += 1

    def dis_student_info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Gender: {self.gender}")
        print(f"Schedule: {self.schedule}")

    @classmethod
    def dis_school_info(cls):
        print("School Information:")
        print(f"School Name: {cls.school_name}")
        print(f"Total Students: {cls.total_students}")
        print(f"Total Classes Offered: {cls.total_classes_offered}")

"""
The @classmethod decorator in Python is used to define a method that operates on the class itself 
rather than on instances of the class. When a method is decorated with @classmethod, 
it receives the class itself (referred to as cls conventionally) as its first argument, 
rather than an instance of the class (conventionally referred to as self).

"""
student1 = Student("John", 15, 10, 'male', ["Math", "Science", "English"])
student2 = Student("Alice", 14, 9, 'female', ["History", "Geography", "Art"])


student1.dis_student_info()
student2.dis_student_info()

Student.dis_school_info()


"""
8. Class Inheritance in Python: Finding GCD (greatest common divisor) and LCM (least common multiple) 
of Numbers and Handling Composite Numbers.


a) Create a Numbers class with a, b, find_gcd(), and find_lcm() methods.

b) Create an EvenNumbers class that inherits from Numbers and overrides find_lcm() to handle even numbers.

c) Create an OddNumbers class that inherits from Numbers and overrides find_lcm() to handle odd numbers.

d) Create a CompositeNumbers class that inherits from EvenNumbers and OddNumbers and overrides find_gcd() 
    to handle composite numbers.

e) Create a CompositeNumbers object with a = 12 and b = 9, and call its find_lcm() and find_gcd() methods.

"""

class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def find_gcd(self):
        x = self.a
        y = self.b
        while y:
            x, y = y, x % y
        return x

    def find_lcm(self):
        gcd = self.find_gcd()
        lcm = (self.a * self.b) // gcd
        return lcm


class EvenNumbers(Numbers):
    def find_lcm(self):
        lcm = super().find_lcm()
        return lcm


class OddNumbers(Numbers):
    def find_lcm(self):
        lcm = super().find_lcm()
        return lcm
        

class CompositeNumbers(EvenNumbers, OddNumbers):
    def find_gcd(self):
        return super().find_gcd()


# Test the implementation
composite = CompositeNumbers(12, 9)
print("LCM:", composite.find_lcm())
print("GCD:", composite.find_gcd())


"""
9. WAP to manage the collections of books in a library in the following  manner:

 Create a Python script that can both read from and write to a CSV file, 
 containing details about each book. Each book's information will include its title, author, publication year, and ISBN number. 
 Your script should be capable of adding new books to the CSV file and listing all the books currently stored in the file.

The program should begin by checking if the CSV file exists.
 If it does not, your script should create it and initialize it with the appropriate headers.
 Then, there should be 2 options: to add a new book or to display all books. 
 When adding a new book, the user should be prompted to enter the title, author, publication year, and ISBN number. 
 This new book should then be added to the CSV file without overwriting the existing entries.
 When choosing to display all books, the script should read from the CSV file and print each book's details.
 
"""




import csv
import os

# Function to check if the CSV file exists
def file_exists(filename):
    return os.path.exists(filename)

# Function to create the CSV file with headers if it doesn't exist
def create_csv(filename):
    headers = ['Title', 'Author', 'Publication Year', 'ISBN']
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

# Function to add a new book to the CSV file
def add_book(filename):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the publication year of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year, isbn])
    print("Book added successfully!")

# Function to display all books stored in the CSV file
def display_books(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)    
        next(reader)  # Skip header row
        for row in reader:
            print("Title:", row[0])
            print("Author:", row[1])
            print("Publication Year:", row[2])
            print("ISBN:", row[3])
            print()

# Main function
def main():
    filename = 'books.csv'
    
    # Check if the CSV file exists, if not create it
    if not file_exists(filename):
        create_csv(filename)
    
    # Main menu
    while True:
        print("\nMain Menu:")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(filename)
        elif choice == '2':
            display_books(filename)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


print(file_exists('books.csv'))




"""
10. WAP to create a pandas dataframe with a list of words and sort them in ascending order. 
The sorted words should be copied to a new file.

"""

import pandas as pd

# List of words
words = ["banana", "apple", "grape", "orange", "mango"]

# Create a pandas DataFrame and sort it
df = pd.DataFrame(sorted(words), columns=["Word"])

# Copy the sorted words to a new file
output_file = "F:\IITM\Mtech 2_sem\data_science\lab_py_files\df to csv.txt"
df.to_csv(output_file, index=False, header=False)

print(f"Sorted words have been copied to {output_file}.")

with open ("F:\IITM\Mtech 2_sem\data_science\lab_py_files\df to csv.txt") as p:
    contents= p.read()
    print(contents)


