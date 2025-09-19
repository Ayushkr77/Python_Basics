# # Functions

# def get_data():
#     return "hello"

# def get_data1():
#     print("hello world")

# print(get_data())
# get_data1()


# # ----------  EXAMPLE 1  ---------- 
# def display_invoice(username, amount, due_date):
#    print(f"Hello {username}")
#    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/01")
# display_invoice("JoeSchmo", 100.01, "01/02")

# # ----------  EXAMPLE 2  ---------- 
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name("spongebob", "squarepants")
# print(full_name)







# Types of arguments
# 1. positional   2. default   3. keyword    4. arbitrary

# # Default Arguments: A default value for certain parameters. default is used when only argument is omitted. make ur functions more flexible, reduces # of arguments


# # ----- EXAMPLE -----
# def net_price(list_price, discount=0, tax=0.05):
#    return list_price * (1 - discount) * (1 - tax)

# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

# # ----- EXERCISE -----
# import time

# def count(end, start=0): 
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")

# count(10)
# count(30, 15)






# # keyword arguments = arguments prefixed with the names of parameters
# # order of the arguments doesn’t matter
# # helps with readability

# # ----- EXAMPLE 1 -----
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello", title="Mr.", last="John", first="James")

# # ----- EXAMPLE 2 -----
# for number in range(1, 11):
#     print(number, end=" ")    # end is a keyword argument

# print("1", "2", "3", "4", "5", sep="-")   # sep is a keyword argument

# # ----- EXERCISE -----
# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1, area=123, first=456, last=7890)
# print(phone_num)







# Arbitrary
# *args= allows u to pass multiple non-key arguments. args mean arguments
# **kwargs= allows u to pass multiple keyword arguments. kwargs mean keyword arguments
# * unpacking operator


# # ----- *ARGS Example 1 -----

# def add(*args):   # can name it anything
#    print(type(args))
#    print(args)
#    total = 0
#    for num in args:
#        total += num
#    return total
# print(add(1, 2, 3, 4))


# # ----- *ARGS Example 2 -----

# def display_name(*args):
#    print(f"Hello", end=" ")
#    for arg in args:
#        print(arg, end=" ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
# print()

# # ----- **KWARGS -----
# print("KWARGS")

# def print_address(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#     for value in kwargs.values():
#         print(value, end=" ")

# print_address(street="123 Fake St.",
#               pobox="P.O Box 777",
#               city="Detroit",
#               state="MI",
#               zip="54321")


# # ----- EXERCISE -----
# def shipping_label(*args, **kwargs):
#     # pass   # pass statement in Python is a null operation
#     for arg in args:
#         print(arg, end=" ")
#     print()

#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     elif "pobox" in kwargs:
#         print(f"{kwargs.get('street')}")
#         print(f"{kwargs.get('pobox')}")
#     else:
#         print(f"{kwargs.get('street')}")

#     print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

# shipping_label("Dr.", "Spongebob", "Squarepants",    # write in same format as in function parameters i.e., first args then kwargs otherwise error
#                street="123 Fake St.",
#                pobox="PO box #1001",
#                city="Detroit",
#                state="MI",
#                zip="54321")






# # Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

# my_list = [1, 2, 3, 4, 5]
# my_tuple = (1, 2, 3, 4, 5)
# my_set = {"apple", "orange", "banana", "coconut"}
# my_name = "Bro Code"
# my_dictionary = {'A': 1, 'B': 2, 'C': 3}

# for item in my_list:
#     print(item)

# # DICTIONARIES
# for key in my_dictionary:
#     print(key)

# for value in my_dictionary.values():
#     print(value)

# for key, value in my_dictionary.items():
#     print(f"{key} = {value}")






# # Membership operators = used to test whether a value or variable is found in a sequence
# # (string, list, tuple, set, or dictionary)
# # 1. in
# # 2. not in

# # --------------------
# # EXAMPLE 1
# # --------------------
# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#    print(f"There is a {letter}")
# else:
#    print(f"{letter} was not found")

# # --------------------
# # EXAMPLE 2
# # --------------------
# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student: ")

# if student in students:
#    print(f"{student} is in this class")
# else:
#    print(f"{student} is NOT in this class")

# # --------------------
# # EXAMPLE 3
# # --------------------
# grades = {
#    "Sandy": 'A',
#    "Squidward": 'B',
#    "Spongebob": 'C',
#    "Patrick": 'D'
# }

# student = input("Enter the name of a student: ")

# if student in grades:
#    print(f"{student}'s grade is {grades[student]}.")
# else:
#    print(f"{student} is not in the dictionary")

# # --------------------
# # EXAMPLE 4
# # --------------------
# email = "BroCode@gmail.com"

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")





# List comprehension = A concise way to create lists in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]
# print(doubles)

# fruits = ["apple", "orange", "banana", "coconut"]
# uppercase_words = [fruit.upper() for fruit in fruits]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(uppercase_words)
# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_numbers = [x for x in numbers if x >= 0]
# negative_numbers = [x for x in numbers if x < 0]
# even_numbers = [x for x in numbers if x % 2 == 0]
# odd_numbers = [x for x in numbers if x % 2 == 1]

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)






# Match-case statement (switch): An alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":     # | is the bitwise OR operator.    In Python 3.10+, you can use the | operator in match statements to match multiple values. Using or will give SyntaxError. So inside match-case, always use |. But in if-elif-else, you should use or.
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:    # default case
#             return False

# print(is_weekend("Monday"))
# print(is_weekend("Sunday"))







# # Module: a file containing code that u want to include in ur program
# # use import to include a module(built in or ur own)
# # useful to break a large program reusable files

# # import math as m   # alias, now we have to write m only, otherwise eror
# # print(m.pi)

# # from math import pi   # prefer above one onlywither with or wothout alias according to ur choice
# # print(pi)  # pi is now in the local scope, we can use it directly


# import module   # while we are importing any module then at that time only the things will get printed that are being printed in that module

# print(module.str)  # pi is now in the local scope, we can use it directly

# result=module.calculate_area(5)
# print(result)  





# # scope resolution: where a variable is visible and accessible
# # LEGB- local, enclosed, global, built-in
# LEGB Rule:
# L – Local: Inside the current function.
# E – Enclosing: Inside outer functions (if nested).
# G – Global: Defined at the top level of the file.
# B – Built-in: Python’s built-in names (like len, range).

# # ----- LOCAL -----

# def func1():
#     x = 1 #local
#     print(x)
# def func2():
#     x = 2 #local
#     print(x)
# func1()
# func2()


# # ----- ENCLOSED -----

# def func1():
#     x = 1 #enclosed
#     def func2():
#         print(x)
#     func2()
# func1()


# # ----- GLOBAL -----

# def func1():
#     print(x)
# def func2():
#     print(x)
# x = 3 #global
# func1()
# func2()


# # ----- BUILT-IN -----

# from math import e 
# def func1():
#     print(e)
# func1()





# x = 10  # Global scope

# def outer():
#     x = 20  # Enclosing scope
#     y=100
    
#     def inner():
#         x = 30  # Local scope
#         print(x)  # Python looks here first -> prints 30
#         print(y)   # inner function can access outer variable-> enclosed
    
#     inner()
#     print(x)  # Prints 20 (enclosing)
    
# outer()
# print(x)  # Prints 10 (global)







# # Couldnt understand

# # if __name__ == '__main__' 

# Every Python file has a special built-in variable called __name__. When a file is run directly, Python sets __name__ = "__main__". When a file is imported as a module in another file, Python sets __name__ = "module_name".

# | `__name__` value | When it occurs               | Code behavior                  |
# | ---------------- | ---------------------------- | ------------------------------ |
# | `"__main__"`     | File is run directly         | Executes code under `if` block |
# | `"module_name"`  | File is imported as a module | Skips code under `if` block    |

# Rule of Thumb:
# Use if __name__ == "__main__": to ensure that certain code only runs when the file is executed directly, not when imported.


# # You can also run a script by right clicking within that script and selecting 'Run'. I forgot about that shortcut while filming this video.

# # if __name__ == __main__: (this script can be imported OR run standalone)
# # Functions and classes in this module can be reused without the main block of code executing

# # Good practice (code is modular, helps readability, leaves no global variables, avoids unintended execution)

# # Ex. library = Import library for functionality.
# #                       When running library directly, display a help page

# # ---------- script1.py ----------
# # This file can run standalone or be imported

# def favorite_food(food):
#     print(f"Your favorite food is {food}")

# def main():
#     print("This is script1")
#     favorite_food("pizza")
#     print("Goodbye!")

# if __name__ == '__main__':
#     main()

# # ---------- script2.py ----------
# # This file should run only standalone

# from script1 import *

# def favorite_drink(drink):
#     print(f"Your favorite drink is {drink}")

# print("This is script2")
# favorite_food("sushi")
# favorite_drink("coffee")
# print('Goodbye!')








# # Python credit card validator program

# # 1. Remove any '-' or ' '
# # 2. Add all digits in the odd places from right to left
# # 3. Double every second digit from right to left.
# #        (If result is a two-digit number,
# #        add the two-digit number together to get a single digit.)
# # 4. Sum the totals of steps 2 & 3
# # 5. If sum is divisible by 10, the credit card # is valid

# sum_odd_digits = 0
# sum_even_digits = 0
# total = 0

# # Step 1
# card_number = input("Enter a credit card #: ")
# card_number = card_number.replace("-", "")
# card_number = card_number.replace(" ", "")
# card_number = card_number[::-1]

# # Step 2
# for x in card_number[::2]:
#     sum_odd_digits += int(x)

# # Step 3
# for x in card_number[1::2]:
#     x = int(x) * 2
#     if x >= 10:
#         sum_even_digits += (1 + (x % 10))
#     else:
#         sum_even_digits += x

# # Step 4
# total = sum_odd_digits + sum_even_digits

# # Step 5
# if total % 10 == 0:
#     print("VALID")
# else:
#     print("INVALID")








# # Python Banking Program

# def show_balance(balance):
#     print("*********************")
#     print(f"Your balance is ${balance:.2f}")
#     print("*********************")

# def deposit():
#     print("*********************")
#     amount = float(input("Enter an amount to be deposited: "))
#     print("*********************")
#     if amount < 0:
#         print("*********************")
#         print("That's not a valid amount")
#         print("*********************")
#         return 0
#     else:
#         return amount

# def withdraw(balance):
#     print("*********************")
#     amount = float(input("Enter amount to be withdrawn: "))
#     print("*********************")

#     if amount > balance:
#         print("*********************")
#         print("Insufficient funds")
#         print("*********************")
#         return 0
#     elif amount < 0:
#         print("*********************")
#         print("Amount must be greater than 0")
#         print("*********************")
#         return 0
#     else:
#         return amount

# def main():
#     balance = 0
#     is_running = True

#     while is_running:
#         print("*********************")
#         print("   Banking Program   ")
#         print("*********************")
#         print("1.Show Balance")
#         print("2.Deposit")
#         print("3.Withdraw")
#         print("4.Exit")
#         print("*********************")
#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             show_balance(balance)
#         elif choice == '2':
#             balance += deposit()
#         elif choice == '3':
#             balance -= withdraw(balance)
#         elif choice == '4':
#             is_running = False
#         else:
#             print("*********************")
#             print("That is not a valid choice")
#             print("*********************")

#     print("*********************")
#     print("Thank you! Have a nice day!")
#     print("*********************")

# if __name__ == '__main__':
#     main()







# # Python Slot Machine
# import random

# def spin_row():
#     symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

#     return [random.choice(symbols) for _ in range(3)]

# def print_row(row):
#     print("**************")
#     print(" | ".join(row))
#     print("**************")

# def get_payout(row, bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == '🍒':
#             return bet * 3
#         elif row[0] == '🍉':
#             return bet * 4
#         elif row[0] == '🍋':
#             return bet * 5
#         elif row[0] == '🔔':
#             return bet * 10
#         elif row[0] == '⭐':
#             return bet * 20
#     return 0

# def main():
#     balance = 100

#     print("*************************")
#     print("Welcome to Python Slots ")
#     print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
#     print("*************************")

#     while balance > 0:
#         print(f"Current balance: ${balance}")

#         bet = input("Place your bet amount: ")

#         if not bet.isdigit():
#             print("Please enter a valid number")
#             continue

#         bet = int(bet)

#         if bet > balance:
#             print("Insufficient funds")
#             continue

#         if bet <= 0:
#             print("Bet must be greater than 0")
#             continue

#         balance -= bet

#         row = spin_row()
#         print("Spinning...\n")
#         print_row(row)

#         payout = get_payout(row, bet)

#         if payout > 0:
#             print(f"You won ${payout}")
#         else:
#             print("Sorry you lost this round")

#         balance += payout

#         play_again = input("Do you want to spin again? (Y/N): ").upper()

#         if play_again != 'Y':
#             break

#     print("*******************************************")
#     print(f"Game over! Your final balance is ${balance}")
#     print("*******************************************")

# if __name__ == '__main__':
#     main()








# Learn oops...




# # object = A "bundle" of related attributes (variables) and methods (functions)
# # Ex. phone, cup, book
# # You need a "class" to create many objects

# # class  = (blueprint) used to design the structure and layout of an object

# class Car:
#    def __init__(self, model, year, color, for_sale):    # necessary to name it __init__ (with double underscores before and after) if you want it to act as a constructor.
#        self.model = model
#        self.year = year
#        self.color = color
#        self.for_sale = for_sale

#    def drive(self):     # it is necessary to write self
#        print("You drive the car")
#        print(f"You drive the {self.model}")
#        print(f"You drive the {self.color} {self.model}")

#    def stop(self):
#        print("You stop the car")
#        print(f"You stop the {self.model}")
#        print(f"You stop the {self.color} {self.model}")

#    def describe(self):
#        print(f"{self.year} {self.color} {self.model}")


# # -------------- main.py --------------
# # from car import Car    # do this thing if you want to import the class from another file

# car1 = Car("Mustang", 2024, "red", False)
# car2 = Car("Corvette", 2025, "blue", True)
# car3 = Car("Charger", 2026, "yellow", True)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# car1.drive()
# car1.stop()
# car3.describe()






# # class variables = Shared among all instances of a class
# # Defined outside the constructor
# # Allow you to share data among all objects created from that class

# class Student:

#    class_year = 2025
#    num_students = 0

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        Student.num_students += 1

# student1 = Student("Spongebob", 30)
# student2 = Student("Patrick", 35)
# student3 = Student("Squidward", 55)
# student4 = Student("Sandy", 27)

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)






# # Inheritance = Allows a class to inherit attributes and methods from another class
# # Helps with code reusability and extensibility
# # class Child(Parent)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is asleep")

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Mouse(Animal):
#     def speak(self):
#         print("SQUEEK!")

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")







# # multiple inheritance = inherit from more than one parent class
# #                                        C(A, B)

# # multilevel inheritance = inherit from a parent which inherits from another parent
# #                                          C(B) <- B(A) <- A

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")



# Method Resolution Order (MRO): have to study






# # Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed. It’s meant to be a blueprint for other classes.
# # They can contain abstract methods, which are declared but have no implementation.
# # Abstract classes benefits:
# # 1. Prevents instantiation of the class itself
# # 2. Requires children to use inherited abstract methods

# | Feature         | Description                                                                         |
# | --------------- | ----------------------------------------------------------------------------------- |
# | Abstract Class  | Blueprint class; cannot instantiate directly; defined using `ABC`.                  |
# | Abstract Method | Method with no implementation in abstract class; must be implemented in subclasses. |
# | Purpose         | Enforce a **contract** for subclasses to implement certain methods.                 |


# from abc import ABC, abstractmethod    # abc = Abstract Base Classes.  Defined by inheriting from ABC (Abstract Base Class) from the abc module.

# class Vehicle(ABC):
# You cannot create Vehicle() because it has an abstract method. Serves as a template for other classes.

#     @abstractmethod
#     def go(self):    # A method declared in an abstract class without implementation. Subclasses must override it to be instantiable.
#         pass    # No implementation, must be defined in child class

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):

#     def go(self):
#         print("You drive the car")

#     def stop(self):
#         print("You stop the car")

# class Motorcycle(Vehicle):

#     def go(self):
#         print("You ride the motorcycle")

#     def stop(self):
#         print("You stop the motorcycle")

# class Boat(Vehicle):

#     def go(self):
#         print("You sail the boat")

#     def stop(self):
#         print("You anchor the boat")

# car = Car()
# car.go()  
# motorcycle = Motorcycle()
# boat = Boat()








# # super() = Function used in a child class to call methods from a parent class (superclass).
# # Allows you to extend the functionality of the inherited methods

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

#     def describe(self):
#         print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
#         super().describe()

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width

#     def describe(self):
#         print(f"It is a square with an area of {self.width * self.width}cm^2")
#         super().describe()

# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height

#     def describe(self):
#         print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
#         super().describe()

# circle = Circle(color="red", is_filled=True, radius=5)
# square = Square(color="blue", is_filled=False, width=6)
# triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

# circle.describe()
# square.describe()
# triangle.describe()








# # Polymorphism = Greek word that means to "have many forms or faces"
# # Poly = Many
# # Morphe = Form

# Search polymorphism in detail. It showing 4 ways: Duck Typing, Method Overriding, Functions working on multiple types, Operator Overloading.

# # TWO WAYS TO ACHIEVE POLYMORPHISM
# # 1. Inheritance = An object could be treated of the same type as a parent class
# # 2. "Duck typing" = Object must have necessary attributes/methods

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# Concrete classes: Circle, Square, Triangle. Search what are concrete classes. Not mandatory that they will inherit, it can be normal classes also

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5

# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping

# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

# for shape in shapes:
#     print(f"{shape.area()}cm²")







# # "Duck typing" = Another way to achieve polymorphism besides Inheritance
# # Object must have the minimum necessary attributes/methods
# # "If it looks like a duck and quacks like a duck, it must be a duck."

# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Car:
#     alive = True
#     def speak(self):
#         print("HONK!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)





# Aggregation = Represents a relationship where one object (the whole)
# Contains references to one or more INDEPENDENT objects (the parts)

# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def list_books(self):
#         return [f"{book.title} by {book.author}" for book in self.books]

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

# library = Library("New York Public Library")

# book1 = Book("Harry Potter...", "J.K. Rowling")
# book2 = Book("The Hobbit", "J. R. R. Tolkein")
# book3 = Book("The Colour of Magic", "Terry Pratchett")

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# print(library.name)

# for book in library.list_books():
#     print(book)





# Aggregation = A relationship where one object contains references to other INDEPENDENT objects
#                           "has-a" relationship

# Composition = The composed object directly owns its components, which cannot exist independently
#                            "owns-a" relationship

# class Engine:
#     def __init__(self, horse_power):
#         self.horse_power = horse_power

# class Wheel:
#     def __init__(self, size):
#         self.size = size

# class Car:
#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel(wheel_size) for wheel in range(4)]

#     def display_car(self):
#         return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

# car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
# car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)
# print(car1.display_car())
# print(car2.display_car())






# Nested class = A class defined within another class
#                            class Outer:
#                                class Inner:

# Benefits: Allows you to logically group classes that are closely related
#                 Encapsulates private details that aren't relevant outside of the outer class
#                 Keeps the namespace clean; reduces the possibility of naming conflicts

# class Company:
#     class Employee:
#         def __init__(self, name, position):
#             self.name = name
#             self.position = position

#         def get_details(self):
#             return f"{self.name} {self.position}"

#     def __init__(self, company_name):
#         self.company_name = company_name
#         self.employees = []

#     def add_employee(self, name, position):
#         new_employee = self.Employee(name, position)
#         self.employees.append(new_employee)

#     def list_employees(self):
#         return [employee.get_details() for employee in self.employees]

# company1 = Company("Krusty Krab")
# company2 = Company("Chum Bucket")

# company1.add_employee("Eugene", "Manager")
# company1.add_employee("Spongebob", "Cook")
# company1.add_employee("Squidward", "Cashier")

# company2.add_employee("Sheldon", "Manager")
# company2.add_employee("Karen", "Assistant")

# for employee in company2.list_employees():
#     print(employee)







# Static methods = A method that belong to a class rather than any object from that class (instance)
# Usually used for general utility functions

# Instance methods - Best for operations on instances of the class (objects)
# Static methods - Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

print(Employee.is_valid_position("Rocket Scientist"))