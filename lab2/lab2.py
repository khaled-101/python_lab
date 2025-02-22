# Question 1 :
# Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.
# operation = "add"
# a, b = 10, 5
# # Expected Output: 15
# ================================================================================
# def calculator(operation,a,b):
#   match operation:
#         case "1" | "add" | "+":
#             return a + b
#         case "2" | "sub" | "-":
#             return a - b
#         case "3" | "div" | "/":
#             if b == 0:
#                 return "Error: Division by zero"
#             return a / b
#         case "4" | "mult" | "*":
#             return a * b
#         case _:
#             return "Invalid operation"
      
      
# operation=input("Enter your operation : \n 1-add (+) \n 2-sub(-) \n 3-div(/) \n 4-mult(*)\n")
# a=float(input("enter the first number : "))
# b=float(input("enter the secound number :"))
# result=calculator(operation,a,b)
# print(f"Your answer is  : {result}")
# ================================================================================
# Question 2 :
# Write a program to filter out even numbers from a list and count how many are left.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Expected Output: [1, 3, 5, 7, 9], Count = 5
# ================================================================================
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered_numbers = []  
# for num in numbers:     
#     if num % 2 != 0: 
#         filtered_numbers.append(num)
# print(f"the new list is {filtered_numbers} , and the count of even numbers is {len(filtered_numbers)}")
# ================================================================================
# Question 3 :
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.
# password = "Pass1234"
# # Expected Output: "Valid Password"
# =====================================================================================
# password=input("enter your password : ")   
# if len(password) < 8:
#         print("Invalid Password: Must be at least 8 characters long.")
#     # Check for at least one uppercase letter
# if not any(char.isupper() for char in password):
#         print("Invalid Password: Must contain at least one uppercase letter.")
    
#     # Check for at least one digit
# if not any(char.isdigit() for char in password):
#         print("Invalid Password: Must contain at least one digit.")
    
# print("Valid Password")
# ====
# Question 4: 
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# ================================================================================
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# new_dic = {}
# new_dic.update(dic1)
# new_dic.update(dic2)
# new_dic.update(dic3)
# print(new_dic )
# =====
# Question 5: 
# takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu
# ======================================================================================
# string = 'abdulrahman' 
# longest=current=string[0]
# for i in range(1,len(string)):
#     if string[i] >= string[i-1]:
#         current+=string[i]
#     else:
#         if len(current) > len(longest):
#             longest = current
#         current = string[i]

# if len(current) > len(longest):
#     print(current)
# else:
#     print(longest)
# =====
# Question 6:
# Write a program to check if a Email meets the following criteria:
# - Ensures the email follows a standard format (e.g., local@domain.com).
# - Does not check if the email actually exists or is deliverable.
# ======================================================================================
# import re
# email=input("enter your e-mail : ")
# pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
# if re.match(pattern,email) :
#     print("Valid Email")
# else:
#     print("Email not Valid")