# # Class methods = Allow operations related to the class
# #                                Take (cls) as the first parameter, which represents the class itself.

# #  Instance methods = Best for operations on instances of the class (objects)
# #  Static methods = Best for utility functions that do not need access to class data
# #  Class methods = Best for class-level data or require access to the class itself

# class Student:

#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     #INSTANCE METHOD
#     def get_info(self):
#         return f"{self.name} {self.gpa}"

#     @classmethod
#     def get_count(cls):
#         return f"Total # of students: {cls.count}"

#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

# student1 = Student("Spongebob", 3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Sandy", 4.0)

# print(Student.get_count())
# print(Student.get_average_gpa())



# Coudnt understand properly static and class methods






# # Magic methods or special methods = Dunder methods (double underscore) __init__, __str__, __eq__
# # They are automatically called by many of Python's built-in operations.
# # They allow developers to define or customize the behavior of objects

# class Book:

#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other):
#         return self.num_pages < other.num_pages

#     def __gt__(self, other):
#         return self.num_pages > other.num_pages

#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"

#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author

#     def __getitem__(self, key):
#         if key == "title":
#             return self.title
#         elif key == "author":
#             return self.author
#         elif key == "num_pages":
#             return self.num_pages
#         else:
#             return f"Key '{key}' was not found"

# book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
# book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
# book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

# print(book1)  # Calls __str__
# print(book1 == book3)  # Calls __eq__
# print(book1 < book2)  # Calls ___lt__
# print(book2 > book3)  # Calls __gt__
# print(book1 + book2)  # Calls __add__
# print("Lion" in book3)  # Calls __contains__
# print(book3['title'])  # Calls __getitem__






# # @property = Decorator used to define a method as a property (it can be accessed like an attribute)
# #                        Benefit: Add additional logic when you read, write, or delete attributes
# #                        Gives you a getter, setter, and deleter method

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"

#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"

#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than zero")

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than zero")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted")

# rectangle = Rectangle(3, 4)






# # Decorator = A function that extends the behavior of another function
# #                      w/o modifying the base function
# #                      Pass the base function as an argument to the decorator

# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("*You add sprinkles 🎊*")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("*You add fudge 🍫*")
#         func(*args, **kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream 🍨")

# get_ice_cream("vanilla")







# whatever code written above, just copy pasted everything. didnt studied.







# # Lambda function = A small anonymous function for a one time use (throw away function)
# # They take any number of arguments, but have only 1 expression
# # Helps keep the namespace clean and is useful with higher-order functions like 'sort()', 'map()', 'filter()', 'reduce()'
# # lambda parameters: expression

# double = lambda x: x * 2
# add = lambda x, y: x + y
# max_value = lambda x, y: x if x > y else y
# min_value = lambda x, y: x if x < y else y
# full_name = lambda first, last: first + " " + last
# is_even = lambda x: x % 2 == 0
# age_check = lambda age: True if age >= 18 else False

# print(double(2))
# print(double(5))
# print(add(3, 4))
# print(max_value(6, 7))
# print(min_value(9, 8))
# print(full_name("Spongebob", "Squarepants"))
# print(is_even(5))
# print(age_check(21))






# # map(function, collection) = Applies a given function to all items in a collection

# def c_to_f(c):
#     return (c * 9/5) + 32

# celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

# fahrenheit_temps = map(c_to_f, celsius_temps)
# print(list(fahrenheit_temps))   # cant do directly print(fahrenheit_temps) because it is a map object or u can use for loop

# fahrenheit_temps_list = list(map(c_to_f, celsius_temps))
# print(fahrenheit_temps_list)

# fahrenheit_temps_lambda = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
# print(fahrenheit_temps_lambda)






# # filter(condition, collection) = return all elements that pass a condition

# grades = [91, 32, 83, 44, 75, 56, 67]
# passing_grades = list(filter(lambda grade: grade >= 60, grades))
# print(passing_grades)






# # reduce(function, collection) = Reduces elements in a collection to a single value
# # For loop is better in most cases so we can avoid using reduce
# # Reduce is better for a functional approach + readability

# from functools import reduce
# prices = [19.99, 1.00, 5.75, 12.99, 10.99]
# total = reduce(lambda x, y: x + y, prices)
# print(f"${total}")








# # SORTING IN PYTHON .sort() or sorted()
# # Lists[], Tuples(), Dictionaries{"":""}, Objects

# # ---------- LISTS ----------
# fruits = ["banana", "orange", "apple", "coconut"]

# fruits.sort()
# # fruits.sort(reverse=True)      # reverse=True for descending order    or first sort normally and then reverse the list fruits.reverse()

# print(fruits)

# # ---------- TUPLES ----------
# fruits = ("banana", "orange", "apple", "coconut")

# fruits = tuple(sorted(fruits))
# # fruits = tuple(sorted(fruits, reverse=True))

# print(fruits)

# # ---------- DICTIONARIES ----------
# fruits = {
#    "banana": 105,
#    "apple": 72,
#    "orange": 73,
#    "coconut": 354
# }

# fruits = dict(sorted(fruits.items()))
# # fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
# # fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
# # fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

# print(fruits)

# # ---------- OBJECTS ----------
# class Fruit:
#    def __init__(self, name, calories):
#        self.name = name
#        self.calories = calories

#    def __repr__(self):
#        return f"{self.name}: {self.calories}"

# fruits = [Fruit("banana", 105),
#               Fruit("apple", 72),
#               Fruit("orange", 73),
#               Fruit("coconut", 354)]

# # fruits = sorted(fruits, key=lambda fruit: fruit.name)
# # fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# # fruits = sorted(fruits, key=lambda fruit: fruit.calories)
# # fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

# print(fruits)





# # recursion = a function that calls itself from within
# #                      helps to visualize a complex problem into basic steps
# #                      problems can be solved more easily iteratively or recursively
# #                      iterative = faster, complex
# #                      recursive = slower, simpler

# # ----- EXAMPLE 1 -----

# # ITERATIVE
# def walk(steps):
#     for step in range(1, steps+1):
#         print(f"You take step #{step}")

# # RECURSIVE
# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps - 1)
#     print(f"You take step #{steps}")

# walk(10)

# # ----- EXAMPLE 2 -----

# # ITERATIVE
# def factorial(x):
#     result = 1
#     if x > 0:
#         for i in range(1, x + 1):
#             result *= i
#         return result

# # RECURSIVE
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)

# print(factorial(10))






# # exception = An event that interrupts the flow of a program
# # (ZeroDivisionError, TypeError, ValueError)
# # 1.try, 2.except, 3.finally

# try:
#     number = int(input("Enter a number: "))
#     print(1 / number)
# except ZeroDivisionError:
#     print("You can't divide by zero IDIOT!")
# except ValueError:
#     print("Enter only numbers please!")
# except Exception:
#     print("Something went wrong!")
# finally:
#     print("Do some cleanup here")






# # Python file detection

# import os

# file_path = "test.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")
#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")








# # Python writing files (.txt, .json, .csv)

# # --------- .txt ---------
# txt_data = "I like pizza!"

# file_path = "output.txt"

# try:
#    with open(file_path, 'w') as file:
#       file.write(txt_data)
#       print(f".txt file '{file_path}' has been created successfully")
# except FileExistsError:
#    print("That file already exists")

# # # --------- .json ---------

# # import json

# # employee = {
# #    "name": "Spongebob",
# #    "age": 30,
# #    "job": "Cook"
# # }

# # file_path = "output.json"

# # try:
# #     with open(file_path, 'w') as file:
# #         json.dump(employee, file, indent=4)

# #     print(f"JSON file '{file_path}' has been created successfully")
# # except FileExistsError:
# #     print("That file already exists!")

# # # --------- .csv---------
# # import csv

# # employees = [["Name", "Age", "Job"],
# #              ["Spongebob", 30, "Cook"],
# #              ["Patrick", 37, "Unemployed"],
# #              ["Sandy", 27, "Scientist"]]

# # file_path = "output.csv"

# # try:
# #     with open(file_path, "w", newline="") as file:
# #         writer = csv.writer(file)
# #         for row in employees:
# #             writer.writerow(row)
# #         print(f"csv file '{file_path}' was created")
# # except FileExistsError:
# #     print("That file already exists!")







# # Python reading files (.txt, .json, .csv)

# # ---------- .txt ----------

# file_path = "output.txt"

# try:
#   with open(file_path, 'r') as file:
#      content = file.read()
#      print(content)
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")

# # # ---------- .json ----------
# # import json

# # file_path = "C:/Users/HP/Desktop/input.json"

# # try:
# #   with open(file_path, 'r') as file:
# #       content = json.load(file)
# #       print(content )
# # except FileNotFoundError:
# #   print("That file was not found")
# # except PermissionError:
# #   print("You do not have permission to read that file")

# # # ---------- .csv ----------
# # import csv

# # file_path = "C:/Users/HP/Desktop/input.csv"

# # try:
# #   with open(file_path, 'r') as file:
# #       content = csv.reader(file)
# #       for line in content:
# #           print(line)
# # except FileNotFoundError:
# #   print("That file was not found")
# # except PermissionError:
# #   print("You do not have permission to read that file")







# # HOW TO MEASURE EXECUTION TIME IN PYTHON

# import time

# start_time = time.perf_counter()

# # YOUR CODE GOES HERE
# for _ in range(100000):
#     pass

# end_time = time.perf_counter()

# elapsed_time = end_time - start_time

# print(f"Elapsed time: {elapsed_time:.5f} seconds")








# # DATES & TIMES
# import datetime

# date = datetime.date(2025, 1, 2)
# today = datetime.date.today()
# print(date)
# print(today)

# time = datetime.time(12, 30, 0)
# now = datetime.datetime.now()
# print(time)
# print(now)

# now = now.strftime("%H:%M:%S %m-%d-%Y")
# print(now)

# target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
# current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target date has passed")
# else:
#     print("Target date has NOT passed")






# # Python Alarm Clock
# import time
# import datetime
# import pygame    # pip install pygame

# def set_alarm(alarm_time):
#     print(f"Alarm set for {alarm_time}")
#     sound_file = "song.mp3"
#     is_running = True

#     while is_running:
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)

#         if current_time == alarm_time:
#             print("WAKE UP! 😴")

#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()

#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)

#             is_running = False

#         time.sleep(1)

# if __name__ == "__main__":
#     alarm_time = input("Enter the alarm time (HH:MM:SS): ")
#     set_alarm(alarm_time)







# # multithreading = Used to perform multiple tasks concurrently (multitasking)
# # Good for I/O bound tasks like reading files or fetching data from APIs

# import threading
# import time

# def walk_dog(first, last):
#    time.sleep(8)
#    print(f"You finish walking {first} {last}")

# def take_out_trash():
#    time.sleep(2)
#    print("You take out the trash")

# def get_mail():
#    time.sleep(4)
#    print("You get the mail")

# # these below functions are working on the same thread
# # walk_dog("Scooby", 7)
# # take_out_trash()
# # get_mail()

# # Now doing all three functions in different threads. Executing these functions concurrently and we're multitasking
# chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# # .join() ensures that all tasks are completed before proceeding. 
# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are complete!")   # If we dont write join above, then this will come in output at first only.








# https://pokeapi.co/
#How to connect to an API using Python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    # print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")





# Python PyQt5...