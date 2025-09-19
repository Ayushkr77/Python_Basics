#        Decorators
#  numpy, pandas, flask     
# Comcurrency, Parallelism

# https://datagrokranalytics-my.sharepoint.com/:w:/r/personal/naveen_gainedi_datagrokr_co/_layouts/15/Doc.aspx?sourcedoc=%7B4E27B701-2BA8-5496-583E-3288A8550749%7D&file=Python_Assignment.docx&action=default&mobileredirect=true


# 2. Define a class Person and its two child classes: Male and Female. All classes have a method "get_gender" which can print "Male" for Male class and "Female" for Female Class.
# Bonus: Make class Person an abstract class and make get_gender an abstract method in the same class. The two child classes must inherit and implement get_gender. i.,e, When trying to initialize an object of class Person, the program must throw an error.
# Hint: Use abc library (comes natively with Python3) https://www.python-course.eu/python3_abstract_classes.php


# class Person:
#     @staticmethod   # bcz dont want to give any parameter in function
#     def get_gender():
#         raise NotImplementedError("Subclass must implement abstract method")   # need to explore this

# class Male(Person):
#     @staticmethod
#     def get_gender():
#         print("Male")
    
# class Female(Person):
#     @staticmethod
#     def get_gender():
#         print("Female")

# if __name__ == "__main__":
#     m=Male()
#     f=Female()
#     m.get_gender()
#     f.get_gender()
#     Male.get_gender()   # Can be called with Male.get_gender() without creating an object if its a static method



# BONUS

# from abc import ABC, abstractmethod

# # Abstract class
# class Person(ABC):
#     @abstractmethod    # we can also make this abstract as well as static, then we can remove self
#     def get_gender(self):
#         pass   # must be implemented by child classes

# class Male(Person):
#     def get_gender(self):
#         return "Male"

# class Female(Person):
#     def get_gender(self):
#         return "Female"

# try:
#     p = Person()   # This will raise an error
# except TypeError as e:
#     print("Error:", e)

# m = Male()
# f = Female()

# print(m.get_gender())   # Male
# print(f.get_gender())   # Female







# 3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
# Hint: Use set() to store a number of values without duplicates.

# orig_list=[12,24,35,24,88,120,155,88,120,155]
# seen=set()  # for empty list
# result=[]
# for i in orig_list:
#     if i not in seen:
#         result.append(i)
#         seen.add(i)
#     else:
#         seen.add(i)
# print(f"Modified list without duplicates: {result}")









# 4. Write a program to generate a 3*5*8 3D array whose each element is 0.

# array_3d=[[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]
# print(array_3d)

# # [0 for _ in range(8)]   It’s a list comprehension in Python.  _ is used as a throwaway variable (because we don’t care about the actual loop index, we only care about repeating something 8 times)








# # 5. Write a binary search function which searches an item in a sorted list. The function should return the index of the element to be searched in the list.

# def binary_search(arr, target):
#     low=0
#     high=len(arr)-1
#     while low<=high:
#         mid=low+(high-low)//2   # for floor division
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]>target:
#             high=mid-1
#         else:
#             low=mid+1
#     return -1

# if __name__=="__main__":
#     arr = [1, 3, 5, 7, 9, 11, 13]
#     target = 7
#     index=binary_search(arr, target)
#     if index!=-1:
#         print(f"Element {target} found at index {index}")
#     else:
#         print("Target element not present in the array")








# # 6. Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

# # A generator expression (or a generator function using yield) does not return a list. Instead, it returns a generator object.

# # def divisible_by_5_and_7(n):
# #     for i in range(n+1):
# #         if i%5==0 and i%7==0:
# #             yield i    # yield instead of return

# # n=int(input("Enter a number: "))

# # gen=divisible_by_5_and_7(n)

# # print(",".join(str(num) for num in gen))



# # Doing in another way. Basically both ways are same. Equivalent using yield

# n=int(input("Enter a number: "))
# gen1=(i for i in range(n+1) if i%5==0 and i%7==0)

# # for i in gen1:
# #     print(i,end=",")    # here , will be printed after last element also,

# # if dont want , to get printed after last element there are solutions

# # Solution 1: using join.    For generators, ",".join(...) is the most Pythonic and simple approach.
# # print(",".join(str(i) for i in gen1))

# # Solution 2:
# first= True    # True and False will be capital only, not true or false
# for i in gen1:
#     if not first:
#         print(",", end="")
#     print(i, end="")
#     first = False








# 7. Assuming that we have some email addresses in the "username@companyname.com" format, write a program to print the company name of a given email address. Both user names and company names are composed of letters only.

# By me
# email_address= input("Enter your email address: ")
# username=""
# company=""
# b1=False
# for i in email_address:
#     if i=="@":
#         b1=True
#     if not b1:
#         username+=i
#         continue
#     if i==".":
#         break
#     if i !="@":
#         company+=i

# print(username)
# print(company)


# Using inbuilt functions
# email = input("Enter your email address: ")
# username, company_part = email.split('@')    # split at '@'
# company_name = company_part.split('.')[0]   # split company part at '.' to remove ".com"
# print("Username is:", username)
# print("Company name is:", company_name)








# 8. Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
# Hints:
# Use map() to generate a list.
# Use Lambda to define anonymous functions.

# numbers = list(range(1, 21))   # generate numbers from 1 to 20
# squares = list(map(lambda x: x**2, numbers))   # use map() with lambda to get squares
# print(squares)









# 9. Implement a program dir_tree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.
# Hint: Use os.listdir and os.path.isdir functions.

# import os
# import sys

# def print_tree(directory, prefix=""):
#     """
#     Recursively prints all files and folders in a directory as a tree.
#     """
#     # list all items in the current directory
#     items = os.listdir(directory)
    
#     for i, item in enumerate(items):
#         path = os.path.join(directory, item)
#         # check if this is the last item to format the tree nicely
#         connector = "└── " if i == len(items) - 1 else "├── "
#         print(prefix + connector + item)
        
#         # if item is a directory, recurse into it
#         if os.path.isdir(path):
#             # add prefix for children
#             extension = "    " if i == len(items) - 1 else "│   "
#             print_tree(path, prefix + extension)

# # get directory from command-line argument
# if len(sys.argv) < 2:
#     print("Usage: python dir_tree.py <directory_path>")
# else:
#     directory = sys.argv[1]
#     if os.path.exists(directory) and os.path.isdir(directory):
#         print(directory)
#         print_tree(directory)
#     else:
#         print("Error: Directory does not exist")










# 10. Write an iterator class ReverseIter, that takes a list and iterates it from the reverse Direction.

# ReverseIter.py
# A custom iterator class that iterates over a list in reverse order

# class ReverseIter:
#     def __init__(self, data):
#         """
#         Constructor: Takes a list (or any iterable) as input.
#         Initializes the index to the last element.
#         """
#         self.data = data
#         self.index = len(data) - 1  # Start from the last element

#     def __iter__(self):
#         """
#         __iter__ should return the iterator object itself.
#         This makes the object iterable (usable in a for loop).
#         """
#         return self

#     def __next__(self):
#         """
#         Returns the next item in reverse order.
#         Raises StopIteration when all items are iterated.
#         """
#         if self.index < 0:
#             raise StopIteration  # No more elements to iterate
#         value = self.data[self.index]  # Get current element
#         self.index -= 1  # Move to previous element
#         return value


# if __name__ == "__main__":
#     my_list = [10, 20, 30, 40, 50]

#     print("Iterating in reverse using ReverseIter:")

#     rev_iter = ReverseIter(my_list)

#     for item in rev_iter:
#         print(item)













# 11. Write a program anti_html.py that takes a URL as argument, downloads the html from web 0and print it after stripping html tags.

# import sys
# import requests
# from bs4 import BeautifulSoup   # pip install beautifulsoup4 requests

# def strip_html(url):
#     try:
#         # Fetch the webpage
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an error for bad response (4xx/5xx)

#         # Parse HTML with BeautifulSoup
#         soup = BeautifulSoup(response.text, "html.parser")
#         # print(soup)

#         # Get only the text (without tags)
#         text = soup.get_text(separator="\n", strip=True)

#         return text

#     except requests.exceptions.RequestException as e:
#         return f"Error fetching URL: {e}"

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python anti_html.py <URL>")
#     else:
#         url = sys.argv[1]
#         result = strip_html(url)
#         print(result)   # 🔹 Make sure to print the result
