# Question 1 a = [10, 20, 30, 20, 40, 50] Remove the first occurance of 20 
# ============================================== 
# a = [10, 20, 30, 20, 40, 50]
# a.remove(20)
# print(a)
# ============================================== 
# Question 2 Remove element at index 1 and return its value in val 
#  ============================================== 
# x= a.pop(1)
# print(x)
# ============================================== 
# Question 3 a = [10, 20, 30, 40, 50, 60, 70] Removes elements from index 1 to index 3 (which are 20, 30, 40) 
# ============================================== 
# a[1:4]=[]
# pint(a)
# ============================================== 
# Question 4 a = [10, 20, 30, 40, 50, 60, 70] Remove all elements
# ==============================================
# a=[]
# print(a)
# ============================================== 
# 5-Write a program that prints the number of times the substring 'iti' occurs in a string 
# ================================================
# string=input("enter your string : ")
# count=string.count("iti")
# print(f"the number of occurence in the string provided is {count}")
# ============================================== 
# 6-application to take a number in binary form from the user, and print it as a decimal
# ============================================== 
# binary_number = input("Enter a binary number: ")
# decimal_value = int(binary_number, 2)
# print(f"The decimal value is: {decimal_value}")
# ============================================== 
# 7-write a code take a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz"
# and if is is divisible by both return "FizzBuzz"
# ============================================== 
# n = int(input("Enter your number: "))
# if n % 3 == 0 and n % 5 == 0:
#     print("Fizzbuzz")
# elif n % 3 == 0:
#     print("Fizz")
# elif n % 5 == 0:
#     print("buzz")
# else:
#     print("wrong number")
# ==============================================================================================
# 8-Ask the user to enter the radius of a circle print its calculated area and circumference
# ==============================================================================================
# import math
# radius_input = input("Enter the radius of the circle: ")
# try:
#     radius = float(radius_input)
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     print("Area:", round(area, 2))
#     print("Circumference:", round(circumference, 2))
# except ValueError:
#     print("invalid input , please enter a integer :)")
# ==============================================================================================
# 9-Ask the user for his name then confirm that he has entered his name (not an empty string/integers).
# then proceed to ask him for his email and print all this data
# ==============================================================================================
# while True:
#     name = input("Enter your name: ").strip()
#     if not name or any(char.isdigit() for char in name):
#         print("Invalid name. Please enter a valid name (non-empty and without numbers).")
#     else:
#         break

# email = input("Enter your email: ")
# print("\nUser Details:")
# print(f"Name: {name}")
# print(f"Email: {email}")

