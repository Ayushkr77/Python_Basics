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










# Example Python class demonstrating Instance, Class, and Static methods

# class Dog:
#     # -------------------------
#     # Class Attribute
#     # -------------------------
#     species = "Canine"   # Shared across all instances of Dog

#     # -------------------------
#     # Constructor / Instance Attributes
#     # -------------------------
#     def __init__(self, name, age):
#         self.name = name  # Unique to each instance
#         self.age = age    # Unique to each instance

#     # -------------------------
#     # Instance Method
#     # -------------------------
#     # Can access instance attributes (self.name, self.age)
#     # Can also access class attributes via self.species
#     def describe(self):
#         return f"{self.name} is {self.age} years old and belongs to {self.species} species."

#     # Another instance method that modifies an instance attribute
#     def birthday(self):
#         self.age += 1
#         print(f"Happy Birthday {self.name}! Age is now {self.age}")

#     # -------------------------
#     # New Instance Method (with extra arguments)
#     # -------------------------
#     # Demonstrates:
#     # - Instance methods can take additional arguments besides 'self'
#     # - Can access/modify class attributes (self.species)
#     # - Cannot modify another instance's attributes unless passed as an object
#     def rename_and_change_species(self, new_name, new_species):
#         print(f"Changing {self.name}'s name to {new_name} and species to {new_species}")
#         self.name = new_name              # Modifies instance attribute of THIS object
#         self.species = new_species        # Modifies class attribute for all instances.  
#         # Note: Cannot directly modify attributes of another instance here
#         # For example, dog2.name = "Max" would require passing dog2 as argument

#         # self.__class__.species = new_species  # Updates class attribute for ALL dogs.   or directly Dog.species = new_species
#         # Rule of Thumb:
#         # self.attr = value → affects only that object.
#         # ClassName.attr = value or self.__class__.attr = value → affects all objects sharing the class attribute.
#         # 3 ways to update class attributes for all instances
# #         | Method                    | Description                                     | Example Code                             |
# # | ------------------------- | ----------------------------------------------- | ---------------------------------------- |
# # | **Direct via Class Name** | Changes class attribute for all instances       | `Dog.species = "Super Canine"`           |
# # | **Class Method**          | Encapsulated way to update class attribute      | `Dog.set_species("Ultra Canine")`        |
# # | **Instance Method**       | From an object, updates class attribute for all | `dog1.__class__.species = "Mega Canine"` |


#     # -------------------------
#     # Class Method
#     # -------------------------
#     # Decorator: @classmethod
#     # Takes cls as the first parameter (refers to the class itself)
#     # Can access/modify class attributes but NOT instance attributes
#     @classmethod
#     def get_species(cls):
#         return f"All dogs belong to the {cls.species} species."

#     @classmethod
#     def set_species(cls, new_species):
#         cls.species = new_species

#     # -------------------------
#     # Static Method
#     # -------------------------
#     # Decorator: @staticmethod
#     # Does NOT take self or cls
#     # Cannot access instance or class attributes
#     # Just a utility function logically related to the class
#     @staticmethod
#     def bark():
#         return "Woof! Woof!"

# # -------------------------
# # USAGE / DEMO
# # -------------------------
# # Creating instances of Dog
# dog1 = Dog("Scooby", 5)
# dog2 = Dog("Buddy", 3)

# # Instance methods
# print(dog1.describe())          # Accesses self attributes and class attribute
# dog2.birthday()                 # Modifies instance attribute

# print("---")

# # Using the new instance method with extra arguments
# dog1.rename_and_change_species("Rex", "Super Canine")
# print(dog1.describe())          # Name and species updated.  # Name: Rex, Species: Super Canine (instance attribute)
# print(dog2.describe())          # Name: Buddy, Species: Canine (still the class attribute)

# print("---")

# # Class methods
# print(Dog.get_species())        # Access class attribute via class
# Dog.set_species("Ultra Canine") # Change class attribute for all instances
# print(dog1.describe())          # Updated species reflected in instance
# print(dog2.describe())          # Updated species reflected here too

# print("---")

# # Static methods
# print(Dog.bark())               # Call via class
# print(dog1.bark())              # Call via instance








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






# | Term      | Description                                                    |
# | --------- | -------------------------------------------------------------- |
# | Decorator | Function that wraps another function to extend/modify behavior |
# | Wrapper   | Inner function inside decorator that adds functionality        |
# | @ Syntax  | Syntactic sugar for applying decorator (`@decorator`)          |
# | Use cases | Logging, timing, authentication, caching                       |


# def decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper

# def say_hello():
#     print("Hello!")

# # Decorating manually
# say_hello = decorator(say_hello)
# say_hello()









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


# There is else block also. Runs only if no exception occurs
# finally block. Always runs (cleanup code, closing files, etc.)

# try → Code that may fail
# except → Handle error
# else → Runs if no error
# finally → Always runs
# raise → Trigger your own error

# raise without handling → program stops (crashes).
# raise inside try-except → error is caught, program continues.






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
# txt_data = "I like pizza!!!"

# file_path = "output.txt"

# try:
#    with open(file_path, 'w') as file:    # 'w' mode = write (creates or overwrites file). Also see 'x' mode
#       file.write(txt_data)
#       print(f".txt file '{file_path}' has been created successfully")
# except FileExistsError:     # except FileExistsError will never run in this case bcz FileExistsError happens only with 'x' mode (exclusive creation). In 'w' mode, Python will overwrite the file if it already exists (no error raised).
#    print("That file already exists")

# # --------- .json ---------

# import json

# employee = {
#    "name": "Spongebob",
#    "age": 30,
#    "job": "Cook"
# }

# file_path = "output.json"

# try:
#     with open(file_path, 'w') as file:
#         json.dump(employee, file, indent=4)  # Converts the Python dictionary → JSON format. Writes it into the file. indent=4 → makes it pretty with indentation.

#     print(f"JSON file '{file_path}' has been created successfully")
# except FileExistsError:
#     print("That file already exists!")

# # # --------- .csv---------
# import csv    # comma separated values

# employees = [["Name", "Age", "Job"],    # header + rows
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 37, "Unemployed"],
#              ["Sandy", 27, "Scientist"]]

# file_path = "output.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")

#     # Alternative (shorter way). Instead of writing rows one by one, you can write all at once:
#     # with open(file_path, "w", newline="") as file:
#     #     writer = csv.writer(file)
#     #     writer.writerows(employees)   # writes entire list of lists

# except FileExistsError:
#     print("That file already exists!")




# | Mode  | Meaning                | Creates file if not exists? | Overwrites existing file?  | Appends if file exists? | Error if file exists?                            |
# | ----- | ---------------------- | --------------------------- | -------------------------- | ----------------------- | ------------------------------------------------ |
# | `'r'` | **Read**               | ❌ No                        | ❌ No                       | ❌ No                    | ✅ Yes (`FileNotFoundError` if file missing)      |
# | `'w'` | **Write**              | ✅ Yes                       | ✅ Yes (erases old content) | ❌ No                    | ❌ No                                             |
# | `'a'` | **Append**             | ✅ Yes                       | ❌ No                       | ✅ Yes (adds to end)     | ❌ No                                             |
# | `'x'` | **Exclusive creation** | ✅ Yes                       | ❌ No                       | ❌ No                    | ✅ Yes (`FileExistsError` if file already exists) |








# # Python reading files (.txt, .json, .csv)

# # ---------- .txt ----------

# file_path = "output.txt"

# try:
#   with open(file_path, 'r') as file:    # with → automatically closes the file when done.
#      content = file.read()    # read entire file as a string
#      print(content)
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")

# # # ---------- .json ----------
# import json

# # file_path = "C:/Users/HP/Desktop/input.json"
# file_path = "output.json"

# try:
#   with open(file_path, 'r') as file:
#       content = json.load(file)    # parse JSON → Python dict/list
#       print(content )
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")

# # # ---------- .csv ----------
# import csv

# # file_path = "C:/Users/HP/Desktop/input.csv"
# file_path = "output.csv"

# try:
#   with open(file_path, 'r') as file:
#       content = csv.reader(file)   # create a CSV reader object
#       for line in content:   # iterate over rows
#           print(line)         # each row is a list
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")







# # HOW TO MEASURE EXECUTION TIME IN PYTHON

# import time

# start_time = time.perf_counter()   # It gives the most precise clock available in Python for measuring short durations. Returns the current value of a performance counter in fractional seconds (float). time.perf_counter() is monotonic: it always moves forward, never backward.

# # YOUR CODE GOES HERE
# for _ in range(100000):
#     pass

# end_time = time.perf_counter()

# elapsed_time = end_time - start_time

# print(f"Elapsed time: {elapsed_time:.5f} seconds")



# Other Timing Functions
# time.time() → wall clock time (affected by system changes).
# time.perf_counter() → best for benchmarking.
# time.process_time() → measures CPU time (ignores sleep, waiting).








# # DATES & TIMES
# import datetime

# date = datetime.date(2025, 1, 2)   # year, month, date. If month or date is out of bounds then error
# today = datetime.date.today()
# print(date)
# print(today)

# time = datetime.time(12, 30, 0)   # makes a time object: 12:30:00.
# now = datetime.datetime.now()
# print(time)
# print(now)

# now = now.strftime("%H:%M:%S %m-%d-%Y")    # strftime() converts a datetime object → formatted string.
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

# .join: Makes the main thread wait until each thread is done. Without .join(), the main program continues immediately → so "All chores are complete!" could print before chores finish. If u want to skip .join, u just have to write .start() as written above

# print("All chores are complete!")   # If we dont write join above, then this will come in output at first only.





# Concurrency = broader concept (managing multiple tasks).
# Multithreading = one technique to implement concurrency.
# Parallelism = actually running things simultaneously (possible with multiple cores).

# All multithreading is concurrency.
# Not all concurrency is multithreading (it could be multiprocessing or async I/O).







# # https://pokeapi.co/
# #How to connect to an API using Python

# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)
#     # print(response)

#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "pikachu"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")









# # Generators
# # A generator is a special kind of iterable that produces items one at a time instead of storing them all in memory.
# # Useful for memory efficiency and lazy evaluation.
# # Generators use the yield keyword instead of return.


# # Basic Generator Function
# def my_generator():
#     yield 1     
#     yield 2
#     yield 3

# gen = my_generator()

# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# # print(next(gen))  # StopIteration error if no more items

# # yield pauses the function and returns a value.
# # The function resumes where it left off on the next next() call.


# # Using a Generator in a Loop
# def squares(n):
#     for i in range(1, n+1):
#         yield i * i

# for val in squares(5):
#     print(val)

# # Values are generated on the fly, not stored in memory.



# # Generator Expression (like list comprehension)
# gen_exp = (x*x for x in range(5))
# for val in gen_exp:
#     print(val)
# # Use parentheses () instead of brackets [].
# # More memory-efficient than creating a list.

# # Memory efficiency of generators vs lists.
# import sys
# big_list = list(range(1000000))
# big_gen = (x for x in range(1000000))
# print("Memory used by list:", sys.getsizeof(big_list))
# print("Memory used by generator:", sys.getsizeof(big_gen))


# # Why Use Generators?
# # Handle large data efficiently.
# # Useful for streaming data or reading large files line by line.
# # Can pause and resume computation.










# # split method

# # ===============================
# # PYTHON STRING SPLIT() DEMO
# # ===============================

# # -------------------------------
# # 1️⃣ Basic split (default: whitespace)
# # -------------------------------
# text = "I love Python"
# words = text.split()  # Splits at spaces by default
# print("Split by space:", words)
# # Output: ['I', 'love', 'Python']

# # -------------------------------
# # 2️⃣ Split with a custom separator
# # -------------------------------
# csv_text = "apple,banana,cherry"
# fruits = csv_text.split(",")  # Splits at commas
# print("Split by comma:", fruits)
# # Output: ['apple', 'banana', 'cherry']

# # -------------------------------
# # 3️⃣ Limiting number of splits
# # -------------------------------
# sentence = "one two three four"
# limited_split = sentence.split(" ", 2)  # Max 2 splits
# print("Limited split (max 2 splits):", limited_split)
# # Output: ['one', 'two', 'three four']

# # -------------------------------
# # 4️⃣ Splitting by other characters
# # -------------------------------
# data = "2025-09-08"
# date_parts = data.split("-")  # Split by dash
# print("Split by dash:", date_parts)
# # Output: ['2025', '09', '08']

# # -------------------------------
# # 5️⃣ Using split on empty string
# # -------------------------------
# empty_text = ""
# result = empty_text.split()
# print("Split on empty string:", result)
# # Output: []

# # -------------------------------
# # 6️⃣ Using rsplit() (split from right)
# # -------------------------------
# sentence2 = "a,b,c,d,e"
# right_split = sentence2.rsplit(",", 2)  # Split at most 2 times from the right
# print("Right split with max 2 splits:", right_split)
# # Output: ['a,b,c', 'd', 'e']











# enumerate

# ===============================
# PYTHON ENUMERATE() DEMO
# ===============================

# -------------------------------
# 1️⃣ Basic enumerate with a list
# -------------------------------
fruits = ["apple", "banana", "cherry"]

print("Basic enumerate:")
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

print("\n------------------------------\n")

# -------------------------------
# 2️⃣ Starting counter at a custom number
# -------------------------------
print("Custom start index:")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# Output:
# 1 apple
# 2 banana
# 3 cherry

print("\n------------------------------\n")

# -------------------------------
# 3️⃣ Using enumerate with a string
# -------------------------------
letters = "Python"
print("Enumerate with a string:")
for index, letter in enumerate(letters):
    print(index, letter)
# Output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

print("\n------------------------------\n")

# -------------------------------
# 4️⃣ Convert enumerate object to a list
# -------------------------------
enum_list = list(enumerate(fruits))
print("Enumerate converted to list:", enum_list)
# Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

print("\n------------------------------\n")

# -------------------------------
# 5️⃣ Using enumerate in more complex loops
# -------------------------------
numbers = [10, 20, 30, 40]
for idx, val in enumerate(numbers):
    print(f"Index {idx} has value {val}")
# Output:
# Index 0 has value 10
# Index 1 has value 20
# Index 2 has value 30
# Index 3 has value 40






# Python PyQt5...