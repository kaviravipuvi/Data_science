# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:09:49 2024

@author: Kaviyarasan PR
"""

"""Design a class named Polygon that initializes with the length of a side.
 Then, derive a class named Square from the Polygon class. 
 Utilize the side length defined in the Polygon class for the Square class. 
 Within the Square class, implement a method called findArea() that calculates and returns 
 the square's area based on its side length. Use __init__() for necessary initialization"""
 
class Polygon(): 
    def __init__(self, length):
         self.length = length

class Square(Polygon):
    def findarea(self):
        return self.length * self.length

p = Polygon(4)
print(p.length)

s = Square(4)
print(s.findarea())

        
"""2.  (a)  Create a class Father with attributes

                    - father_name (string), father_age (int), father_talents (set of strings)

                Create a class Mother with attributes:

                    - mother_name (string), mother_age (int), mother_talents (set of strings)

                 Create a class Child that inherits both father and mother with attributes: 

                    - child_name (string), child_age (int), child_gender(string)

 (b) Create a function getChildDetails() in Child to input the details of the child, it’s father and mother and printChildDetails() 
 to print the details using     printChildDetails()

 (c) Create an object of class Child and read the details by invoking getChildDetails() and display the details entered.

(d) Create a function displayTalents() in class Child that displays the talents of the child inherited from father and mother. 
A talent is inherited to a child if both the parents possess it.
"""
class Father:
    def __init__(self, f_name, f_age, f_talents):
        self.f_name = str(f_name)
        self.f_age = int(f_age)
        self.f_talents = str(f_talents)

class Mother:
    def __init__(self, m_name, m_age, m_talents):
        self.m_name = str(m_name)
        self.m_age = int(m_age)
        self.m_talents = str(m_talents)

class Child(Father, Mother):
    def __init__(self, c_name="", c_age=0, c_gender="", 
                 f_name="", f_age=0, f_talents=set(), 
                 m_name="", m_age=0, m_talents=set()):
        Father.__init__(self, f_name, f_age, f_talents)
        Mother.__init__(self, m_name, m_age, m_talents)
        self.c_name = str(c_name)
        self.c_age = int(c_age)
        self.c_gender = str(c_gender)
    
    def getchilddetails(self):
        self.f_name = str(input("Enter the father's name: "))
        self.m_name = str(input("Enter the mother's name: "))
        self.c_name = str(input("Enter the child's name: "))
        self.f_age = int(input("Enter the father's age: "))
        self.f_talents = str(input("Enter the father's talents separated by comma: ")).split(",")
        self.m_age = int(input("Enter the mother's age: "))
        self.m_talents = str(input("Enter the mother's talents separated by comma: ")).split(",")
        self.c_gender = str(input("Enter the child's gender: "))
        self.c_age= int(input("Enter the child's age:"))
    
    def printchilddetails(self):
        print("\nChild Details:")
        print(f"Name: {self.c_name}")
        print(f"Age: {self.c_age}")
        print(f"Gender: {self.c_gender}")
            
        print("\nFather Details:")
        print(f"Name: {self.f_name}")
        print(f"Age: {self.f_age}")
        print(f"Talents: {', '.join(self.f_talents)}")
            
        print("\nMother Details:")
        print(f"Name: {self.m_name}")
        print(f"Age: {self.m_age}")
        print(f"Talents: {', '.join(self.m_talents)}")

    def displayTalents(self):
        inherited_talents = set(self.f_talents).intersection(set(self.m_talents))
        print("\nInherited Talents:")
        if inherited_talents:
            print(", ".join(inherited_talents))
        else:
            print("No talents inherited.")


child = Child()
child.getchilddetails()
child.printchilddetails()
child.displayTalents()

""" 3.  Text File Input Output

         Create a .txt (text) file and use the pledge of India as the content of the text file.

         Write a python program that reads this text file, processes it by counting the number of occurrences of each word in the file, and then writes the result back to a          new text file.

"""



def count_word_occurrences(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()  
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts

def write_word_occurrences(word_counts, output_file_path):
    with open(output_file_path, 'w') as file:
        for word, count in word_counts.items():
            file.write(f"{word}: {count}\n")


input_file_path = "F:\IITM\Mtech 2_sem\data_science\lab_py_files\pledge.txt"
output_file_path = "F:\\IITM\Mtech 2_sem\data_science\lab_py_files\\New Text Document.txt"


word_counts = count_word_occurrences(input_file_path)

write_word_occurrences(word_counts, output_file_path)

print("Word occurrences counted and written to 'F:\\IITM\Mtech 2_sem\data_science\lab_py_files\\New Text Document.txt.' ")


"""4.  For a restaurant, create a parent class ‘Bill’ which has the properties as ‘
Customer  name’, ‘Table Number’ and ‘Order’ of which the name, order are strings and table  number is
 a positive integer. Define a method to extract the order details from the string and return a
 2-D array of ordered items & their number. Create a child class ‘ 'Restaurant Bill’ 
 which has a property called ‘Price list’ of the items and has a method to calculate 
 the total bill amount by using the price list and order details. Also have a   
 method to print the complete bill for the customer including taxes and service charges.

     The strings will be of the following format:

     #Name: “Akshay” (Name of the customer)

     #Table Number: 7 (Table Number)

     #Order: “Item1x1,Item2x3,Item3x1,…” (ItemxNumber needed)

     #Price List: “Item1-100,Item2-70,Item3-250,...” (Item-Price)


5. For the previous question( restaurant Bill) - take name, table no, 
    order details from a file, price list from another file and print the whole bill to the new file.
"""
class Bill:
    def __init__(self, c_name, t_number, order):
        self.c_name = c_name
        self.t_number = t_number
        self.order = order
        self.order_details = self.extract_order_details()

    def extract_order_details(self):
        order_details = []
        items = self.order.split(',')
        for item in items:
            item_name, quantity = item.split('x')
            order_details.append([item_name.strip(), int(quantity)])
        return order_details

class RestaurantBill(Bill):
    def __init__(self, c_name, t_number, order, price_list_file):
        super().__init__(c_name, t_number, order)
        self.price_list = self.load_price_list(price_list_file)

    def load_price_list(self, price_list_file):
        price_list = {}
        with open(price_list_file, 'r') as file:
            for line in file:
                item, price = line.strip().split('-')
                price_list[item] = float(price)
        print(price_list)
        return price_list

    def calculate_total_bill(self):
        total_bill = 0
        print(self.order_details)
        for item, quantity in self.order_details:
            # print(item, quantity)
            total_bill += self.price_list[item] * quantity
            
        service_tax = 0.05 * total_bill
        total_bill_with_service_tax = total_bill + service_tax

        return total_bill, total_bill_with_service_tax


    def print_bill(self, bill_file):
        total_bill, total_bill_with_service_tax = self.calculate_total_bill()

        with open(bill_file, 'w') as file:
            file.write(f"________ HOTEL TAJ_______ \n")
            file.write(f"Customer Name: {self.c_name}\n")
            file.write(f"Table Number: {self.t_number}\n")
            file.write("Ordered Items:\n")
            for item, quantity in self.order_details:
                file.write(f"{item}: {quantity}\n")
            file.write(f"Total Bill (Without Service Tax): {total_bill}\n")
            file.write(f"Total Bill with Service Tax: {total_bill_with_service_tax}\n")
            file.write(f"THANK YOU. VISIT AGAIN")


# Usage
c_name = "Akshay"
t_number = 7
order = "Item1x1,Item2x3,Item3x1"
price_list_file = "F:\IITM\Mtech 2_sem\data_science\lab_py_files\items_list.txt"

restaurant_bill = RestaurantBill(c_name, t_number, order, price_list_file)
restaurant_bill.print_bill("F:\\IITM\Mtech 2_sem\\data_science\\lab_py_files\\final_bill.txt")
print("updated the bill. Please check")