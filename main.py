# print("Hello World")


# # Variable = A container for a value (string, integer, float, boolean). A variable behaves as if it was the value it contains

# # Strings
# first_name = "Bro"
# food = "pizza"
# email = "Bro123@fake.com"

# # Integers
# age = 25
# quantity = 3
# num_of_students = 30

# # Float
# price = 10.99
# gpa = 3.2
# distance = 5.5

# # Boolean
# is_student = True
# for_sale = False
# is_online = True

# # An f-string (short for formatted string literal) is a way to embed expressions inside string literals using Python. It makes string formatting more readable and concise.
# print(f"Hello {first_name}")
# print(f"You are {age} years old")
# print(f"Your gpa is: {gpa}")

# if is_student: print("You are a student")
# else:
#     print("You are NOT student")




# # 1. Basic variable substitution
# fruit = "apple"
# print(f"I like {fruit}.")

# # 2. Expression inside the f-string
# a = 5 
# b = 10
# print(f"Sum of a and b is {a + b}")

# # 3. Formatting numbers (2 decimal places)
# pi = 3.14159
# print(f"Pi rounded to 2 decimals: {pi:.2f}")

# # 4. Using dictionary inside f-string
# data = {"name": "Ayush", "age": 21}
# print(f"{data['name']} is {data['age']} years old.")

# # 5. Aligning text (left, center, right)
# name = "Ayush"
# print(f"|{name:<10}|")  # Left align
# print(f"|{name:^10}|")  # Center align
# print(f"|{name:>10}|")  # Right align

# # 6. Formatting with leading zeros
# num = 7
# print(f"Padded number: {num:03}")  # Output: 007

# # 7. Embedding function calls
# def greet():
#     return "Hello"

# print(f"Greeting: {greet()}")

# # 8. Multi-line f-string
# first_name = "Ayush"
# last_name = "Kumar"
# print(f"""
# Full Name:
# First: {first_name}
# Last: {last_name}
# """)

# # 9. Using f-strings with calculations inside
# length = 5
# width = 3
# print(f"Area of rectangle: {length * width}")








# # type casting = The process of converting a value of one data type to another (string, integer, float, boolean)
# # Explicit vs Implicit

# # explicit
# name = "Bro"
# age = 21
# gpa = 1.9
# student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student)) 

# age = float(age)
# print(age)

# gpa = int(gpa)
# print(gpa)

# student = str(student)
# print(student)

# name = bool(name)   # if empty string or 0 value then it will be false
# print(name)


# # implicit
# x=2
# y=2.0
# print(x+y)  # it will convert x to float and then add both values





# # Input 

# # EXERCISE 1 MAD LIBS
# # ------------------------------------------------
# adjective1 = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# adjective2 = input("Enter an adjective: ")
# verb = input("Enter a verb: ")
# adjective3 = input("Enter an adjective: ")

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw {noun}.")
# print(f"{noun} was {adjective2} and {verb}ing.")
# print(f"I was {adjective3}!")

# # ------------------------------------------------
# # EXERCISE 2 AREA CALC
# # ------------------------------------------------
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))

# area = length * width
# print(f"The area is: {area}cm^2")

# # ------------------------------------------------
# # EXERCISE 3 SHOPPING CART
# # ------------------------------------------------
# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))

# total = price * quantity

# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: ${round(total, 2)}")






# # in built functions

# x=3.14
# y=4
# z=5

# print(round(x))
# print(round(x,1)) # rounds to 2 decimal places

# y=-1
# print(abs(y)) # absolute value

# result=max(x,y,z)
# print(result)

# print(pow(4,3))

# numbers = [4, 7, 1, 9, 3]
# print(max(numbers)) 






# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
#     print("Make sure to carry your ID card.")
# elif age > 0:
#     print("You are not eligible to vote yet.")
#     print(f"Wait {18 - age} more years.")
# else:
#     print("Age cannot be negative.")
#     print("Please enter a valid age.")
# print("if elif else finished.")






# # logical operators = used on conditional statements

# #              and = checks two or more conditions are True
# #               or = checks if at least one condition is True
# #              not = True if condition is False, and vice versa

# temp = 20
# sunny = True

# if temp <= 0 or temp >= 30:
#     print("The temperature is bad")
# else:
#     print("The temperature is good")

# if not sunny:
#     print("It is cloudy")
# else:
#     print("It is sunny")





# # conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# #                                             Print or assign one of two values based on a condition
# #                                             X if condition else Y

# num = 5
# a = 6
# b = 7
# age = 13
# temperature = 20
# user_role = "guest"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"






# # -------------------------------
# # STRING METHODS
# # -------------------------------

# # Taking user input
# name = input("Enter your name: ")
# phone_number = input("Enter your phone #: ")

# # String operations on 'name'
# length = len(name)                   # Gets the length of the name
# index = name.find(" ")              # Finds the index of the first space
# capitalized = name.capitalize()     # Capitalizes first letter, rest lowercase
# upper_name = name.upper()           # Converts entire name to uppercase
# lower_name = name.lower()           # Converts entire name to lowercase
# is_digit = name.isdigit()           # Checks if name is all digits
# is_alpha = name.isalpha()           # Checks if name is all alphabets (no spaces)

# # String operations on 'phone_number'
# space_count = phone_number.count(" ")       # Counts number of spaces
# cleaned_phone = phone_number.replace("-", "")  # Removes all dashes from phone number

# # Display results
# print("\n--- Results ---")
# print(f"Original Name: {name}")
# print(f"Length of name: {length}")
# print(f"Index of first space: {index}")
# print(f"Capitalized: {capitalized}")
# print(f"Uppercase: {upper_name}")
# print(f"Lowercase: {lower_name}")
# print(f"Is name all digits? {is_digit}")
# print(f"Is name all alphabets (no space)? {is_alpha}")
# print(f"Spaces in phone number: {space_count}")
# print(f"Phone number without dashes: {cleaned_phone}")


# # -------------------------------
# #        EXERCISE
# # -------------------------------
# username = input("Enter a username: ")

# if len(username) > 12:
#    print("Your name can't be more than 12 characters")
# elif not username.find(" ") == -1:
#    print("Your username can't contain spaces")
# elif not username.isalpha():
#    print("Your username can't contain digits")
# else:
#    print(f"Welcome {username}!")






# # indexing = accessing elements of a sequence using [] (indexing operator)
# # [start : end : step]

# credit_number = "1234-5678-9012-3456"

# print(credit_number[0])        # Prints the first character → '1'
# print(credit_number[0:4])      # Prints characters from index 0 to 3 → '1234'
# print(credit_number[:4])       # Same as above (start is optional) → '1234'
# print(credit_number[4:8])      # Prints characters from index 4 to 7 → '-567'
# print(credit_number[4:])       # Prints from index 4 to the end → '-5678-9012-3456'
# print(credit_number[-1])       # Prints the last character → '6'
# print(credit_number[-4:])      # Prints last 4 characters → '3456'
# print(credit_number[::2])      # Prints every 2nd character → '1357-013-46'
# print(credit_number[::3])      # Prints every 3rd character → '1470-4-6'


# # EXERCISE 1
# credit_number = "1234-5678-9012-3456"
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# # EXERCISE 2
# credit_number = "1234-5678-9012-3456"
# credit_number = credit_number[::-1]    # [start:stop:-1]	Reverses part from start to stop-1. couldnt understand
# print(credit_number)


# email = input("Enter your email: ")
# username = email[:email.index("@")]
# domain = email[email.index("@") + 1:]
# print(f"Your username is {username} and domain is {domain}")





# # format specifiers = {:flags} format a value based on what flags are inserted

# # .(number)f = round to that many decimal places
# # :(number) = allocate that many spaces
# # :0(number) = allocate and zero pad that many spaces
# # :< = left justify
# # :> = right justify
# # :^ = center align
# # :+ = use a plus sign to indicate positive value
# # := = place sign to leftmost position
# # :  = insert a space before positive numbers
# # :, = comma separator
# # :% = percentage format

# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34

# print(f"price1 is: ${price1:.2f}")       # Rounded to 2 decimal places → $3.14
# print(f"price2 is: ${price2:10}")        # Allocated 10 spaces → right aligned by default
# print(f"price3 is: ${price3:010}")       # Zero-padded to 10 spaces → $0000012.34
# print(f"price1 is: ${price1:<10.2f}")    # Left justified in 10 spaces → '3.14      '
# print(f"price2 is: ${price2:>10.2f}")    # Right justified in 10 spaces → '    -987.65'
# print(f"price3 is: ${price3:^10.2f}")    # Center aligned in 10 spaces → '   12.34  '
# print(f"price1 is: ${price1:+.2f}")      # Shows + sign for positive → '+3.14'
# print(f"price2 is: ${price2:=10.2f}")    # Sign placed to the leftmost position → '-   987.65'
# print(f"price1 is: ${price1: .2f}")      # Inserts space before positive → ' 3.14'
# print(f"price is: ${-981234117.65:,.2f}")      # Adds comma separators → '-987.65'
# print(f"price1 is: {price1:.2%}")        # Percentage format → '314.16%'.    It multiplies the number by 100. Appends a percent sign %. Rounds to 2 decimal places








# # while loop = perform some code WHILE some condition remains true

# # ---------------- EXAMPLE 1 ----------------

# name = input("Enter your name: ")

# while name == "":
#    print("You did not enter your name!")
#    name = input("Enter your name: ")

# print(f"Hello {name}")

# # ---------------- EXAMPLE 2 ----------------

# age = int(input("Enter your age: "))

# while age < 0:
#    print("Age can't be negative")
#    age = int(input("Enter your age: "))

# print(f"You are {age} years old")


# # ---------------- EXAMPLE 3 ----------------

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#    print(f"You like {food}")
#    food = input("Enter another food you like (q to quit): ")

# print("bye")

# # ---------------- EXAMPLE 4 ----------------

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"You picked the number {num}")






# # for loops = execute a block of code a fixed number of times.
# #                     You can iterate over a range, string, sequence, etc.

# # ---------------- EXAMPLE 1 ----------------

# for x in range(1, 11):     
#    print(x, end=" ")     # By default, print() ends with a newline (\n). You can change it to a space or empty string
# print("\n")

# # Using one print() with multiple arguments
# # name = "Ayush"
# # age = 21
# # print("Name:", name, "Age:", age)


# # ---------------- EXAMPLE 2 ----------------

# for x in reversed(range(1, 11)):
#    print(x)

# print("Happy New Year!")

# # ---------------- EXAMPLE 3 ----------------

# for x in range(1, 11, 2):
#    print(x)
# print("Happy New Year!")

# # ---------------- EXAMPLE 4 ----------------

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#    print(x)
# print("Happy New Year!")

# # ---------------- CONTINUE ----------------

# for x in range(1, 21):
#    if x == 13:
#        continue
#    else:
#        print(x)

# # ---------------- BREAK ----------------

# for x in range(1, 21):
#    if x == 13:
#        break
#    else:
#        print(x)



# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit, end=", ")



# prices = [3.14159, 2.71828, 1.41421]
# for price in prices:
#     print(f"${price:.2f}", end="  ")





# # nested loop = A loop within another loop (outer, inner)
# #                          outer loop:
# #                              inner loop:

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter a symbol to use: ")

# for x in range(rows):
#    for y in range(columns):
#        print(symbol, end="")
#    print()






# # Countdown timer program

# import time
# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)    # Pauses execution for 1 second

# print("TIME'S UP!")






# # List  = [] ordered and changeable. Duplicates OK
# # Set   = {} unordered and immutable, but can Add/Remove values. NO duplicates
# # Tuple = () ordered and unchangeable. Duplicates OK. FASTER





# # list_examples.py

# # ✅ Creating Lists
# empty_list = []                                # An empty list
# numbers = [1, 2, 3, 4, 5]                      # A list of integers
# mixed = [1, "hello", 3.14, True]              # A list with mixed data types
# nested = [[1, 2], [3, 4]]                      # A 2D (nested) list

# # ✅ Accessing Elements
# print("First element:", numbers[0])            # Accessing first element → 1
# print("Last element:", numbers[-1])            # Accessing last element → 5
# print("Nested element:", nested[1][0])         # Access nested list element → 3

# # ✅ Modifying Lists
# numbers[1] = 20                                 # Change value at index 1
# print("Modified list:", numbers)               # Output modified list

# # ✅ List Methods
# numbers.append(6)                              # Add 6 at the end
# numbers.insert(2, 100)                         # Insert 100 at index 2
# numbers.remove(3)                              # Remove the first occurrence of 3
# popped = numbers.pop()                         # Remove and return the last element
# print("Popped element:", popped)               # Print popped element
# numbers.sort()                                 # Sort the list in ascending order
# numbers.reverse()                              # Reverse the list
# print("List after sort and reverse:", numbers) # Output final list

# # ✅ Built-in Functions
# print("Length:", len(numbers))                 # Length of list
# print("Sum:", sum(numbers))                    # Sum of elements
# print("Max:", max(numbers))                    # Maximum value
# print("Min:", min(numbers))                    # Minimum value

# # ✅ Looping Through a List
# print("Looping through list:")
# for num in numbers:                            # Loop through each element
#     print(num)

# # With index
# print("Looping with index:")
# for i, val in enumerate(numbers):              # Get both index and value
#     print(f"Index {i}: {val}")

# # ✅ List Comprehension
# squares = [x**2 for x in range(5)]             # Square of numbers from 0 to 4
# print("Squares using list comprehension:", squares)





# # Little more about lists
# fruits=["apple","orange","banana","mango"]

# # dir and help. Its not only for lists but we can use it anywhere. list, string, dict, int,...
# # dir() and help() are two built-in functions in Python that can be used to get information

# # print(dir(fruits))    #  dir() – To List Attributes and Methods
# # print(help(fruits))   #To Get Documentation
# print(help(fruits.append))    # or just help(fruits.append) to Get Documentation of append() method

# print("apple" in fruits)
# print("apple" not in fruits)
# print(fruits.index("apple"))
# print(fruits.count("apple"))
# fruits.clear()
# print(fruits)  # Output: []








# # Sets
# fruits={"apple","orange","banana","mango"}
# print(fruits)    # order may vary because sets are unordered collections in Python
# # we cannot access elements by index in sets as they are unordered

# fruits.add("pineapple")
# print(fruits)    
# fruits.remove('pineapple')
# print(fruits)    
# fruits.pop()
# print(fruits)    





# # Tuples
# fruits=("apple","orange","banana","mango")
# print(fruits)
# print(fruits[0])    
# print(fruits[0:3])   
# print(fruits[0:3:2])   
# # fruits[0]="hello"   will cause error as unchangeable
# print(fruits)





# # Shopping cart exercise
# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- YOUR CART -----")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price

# print()
# print(f"Your total is: ${total}")






# # Here are a few different 2d collection combinations:

# # 2D list of lists
# num_pad = [[1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 9],
#                       ["*", 0, "#"]]

# print(num_pad)

# # 2D list of tuples
# num_pad = [(1, 2, 3),
#                       (4, 5, 6),
#                       (7, 8, 9),
#                       ("*", 0, "#")]
# print(num_pad)


# # 2D list of sets
# num_pad = [{1, 2, 3},
#                       {4, 5, 6},
#                       {7, 8, 9},
#                       {"*", 0, "#"}]
# print(num_pad)

# # 2D tuple of lists
# num_pad = ([1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 9],
#                       ["*", 0, "#"])
# print(num_pad)

# # 2D tuple of tuples
# num_pad = ((1, 2, 3),
#                       (4, 5, 6),
#                       (7, 8, 9),
#                       ("*", 0, "#"))
# print(num_pad)

# # 2D tuple of sets
# num_pad = ({1, 2, 3},
#                       {4, 5, 6},
#                       {7, 8, 9},
#                       {"*", 0, "#"})
# print(num_pad)

# # # 2D set of lists (NOT VALID)
# # num_pad = {[1, 2, 3],
# #                       [4, 5, 6],
# #                       [7, 8, 9],
# #                       ["*", 0, "#"]}
# # # This will raise a TypeError: unhashable type: 'list'

# # # 2D set of tuples
# # num_pad = {(1, 2, 3),
# #                       (4, 5, 6),
# #                       (7, 8, 9),
# #                       ("*", 0, "#")}
# # # This will raise a TypeError: unhashable type: 'tuple'

# # # 2D set of sets (NOT VALID)
# # num_pad = {{1, 2, 3},
# #                       {4, 5, 6},
# #                       {7, 8, 9},
# #                       {"*", 0, "#"}}
# # # This will raise a TypeError: unhashable type: 'set'


# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

# print(num_pad)








# QUIZ GAME

# questions = ("How many elements are in the periodic table?: ",
#                        "Which animal lays the largest eggs?: ",
#                        "What is the most abundant gas in Earth's atmosphere?: ",
#                        "How many bones are in the human body?: ",
#                        "Which planet in the solar system is the hottest?: ")

# options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#                    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#                    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#                    ("A. 206", "B. 207", "C. 208", "D. 209"),
#                    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("----------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1

# print("----------------------")
# print("       RESULTS        ")
# print("----------------------")

# print("answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")







# # dictionary =  a collection of {key:value} pairs
# # ordered and changeable. No duplicates

# capitals = {"USA": "Washington D.C.",
#                     "India": "New Delhi",
#                     "China": "Beijing",
#                     "Russia": "Moscow"}


# # print(dir(capitals))
# # print(help(capitals))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals.get("USA"))
# print(capitals["USA"])
# print(capitals.get("Japan"))

# # if capitals.get("Russia"):
# #    print("That capital exists")
# # else:
# #    print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# print(capitals)


# # # print(capitals.pop("USA"))
# # capitals.pop("China")
# # print(capitals)

# # print(capitals.popitem())
# # print(capitals)
# # capitals.popitem()
# # print(capitals)

# # capitals.clear()
# # print(capitals)  # prints: {}


# print(f"length of the dict is {len(capitals)}")  

# # keys = capitals.keys()
# for key in capitals.keys():
#   print(key)

# # values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.items():
#    print(f"{key}: {value}")






# # Concession stand program

# menu = {"pizza": 3.00,
#                "nachos": 4.50,
#                "popcorn": 6.00,
#                "fries": 2.50,
#                "chips": 1.00,
#                "pretzel": 3.50,
#                "soda": 3.00,
#                "lemonade": 4.25}
# cart = []
# total = 0

# print("--------- MENU ---------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("------------------------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print("------ YOUR ORDER ------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total is: ${total:.2f}")






# Random

# import random

# low = 1
# high = 100
# options = ("Rock", "Paper", "Scissors")
# cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# numberFloat = random.random()  # a random number between 0 and 1.  0.0 <= number < 1.0
# print(numberFloat)
# print(int(numberFloat*10))
# number = random.randint(low, high)   # low and high are inclusive range
# print(number)
# choice = random.choice(options)   # random element from the list
# print(choice)

# print(cards)
# random.shuffle(cards)
# print(cards)




# # -------------- NUMBER GUESSING GAME --------------

# import random

# low = 1
# high = 10
# guesses = 0
# number = random.randint(low, high)

# while True:
#    guess = int(input(f"Enter a number between ({low} - {high}): "))
#    guesses += 1

#    if guess < number:
#        print(f"{guess} is too low")
#    elif guess > number:
#        print(f"{guess} is too high")
#    else:
#        print(f"{guess} is correct!")
#        break

# print(f"This round took you {guesses} guesses")






# # ROCK PAPER SCISSORS

# import random

# options = ("rock", "paper", "scissors")
# running = True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")

#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False

# print("Thanks for playing!")







# # Here are the Unicode characters I use for drawing the dice.
# # Youtube has strange spacing, so the ASCII art looks warped in the description. 
# # It should still work if you copy and paste it into PyCharm.

# import random

# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # PRINT VERTICALLY
# # for die in range(num_of_dice):
# #    for line in dice_art.get(dice[die]):
# #        print(line)

# # PRINT HORIZONTALLY
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"total: {total}")








import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters     # string.whitespace
# print(chars)
chars = list(chars)
key = chars.copy()
print(chars)
print(key)

random.shuffle(key)

print(key)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")