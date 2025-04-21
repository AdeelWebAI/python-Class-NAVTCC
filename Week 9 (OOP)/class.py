#



















# 1. Write a Python program to declare a variable x with value "50", convert it to an integer, add 10 to it, and print the result.
# # Given the list:
# # numbers = [5, 10, 15, 20, 25]
# # Replace 15 with 50.
# # Add 30 at the beginning of the list.
# # Remove 10 from the list.
# # Print the last element of the list using negative indexing.

# x = '50'
# # convert into integer
# convert_int_x = int(x) + 10
# print(convert_int_x)

# numbers = [5, 10, 15, 20, 25]
# print(f'orignal is {numbers}')
# numbers[2] = 50
# print(f"After changeing 15 to 50 list is :{numbers}")

# # Adding 30 at he beginning of the list 
# numbers.insert(0,30)
# print(f"Adding 30 at the beginning of the list: {numbers}")

# # remove 10 from the list 
# del numbers[2]
# print(f"Remove 10 from the list:{numbers}")

# print(f'The last element of the list using neg-index : {numbers[-1]}')

# # 2. Write a Python program that takes a string input and checks whether it contains the word "Python" (case insensitive).
# # Given a dictionary:
# # student = {"name": "Sarah", "age": 21, "course": "AI"}
# # Change "age" to 22.
# # Add a new key "grade" with value "A".
# # Remove the key "course".
# # Print all keys and values separately.
# # Create a tuple with values (10, 20, 30, 40, 50).
# # Print the third element.
# # Unpack the tuple into separate variables and print them.

# user_input = input('Enter:')
# if "Python" in user_input:
#     print(f'"Pyhton" in the string :"{user_input}"')
# else:
#     print(f'"Python" is not in the string :"{user_input}"')

# student = {"name": "Sarah", "age": 21, "course": "AI"}
# student["age"] = 22
# print(f'After changing the Age of student dict is {student}')

# student['grade'] = 'A'
# print(f'After adding grade in the dict {student}')

# del student['course']
# print(f'After removing the course from the dict is {student}')

# print(f'All keys in the dictionary is:{student.keys()}')

# print(f'All values in the dictionary is:{student.values()}')

# mytuple = (10, 20, 30, 40, 50)

# print(f'the third item in the{mytuple} is {mytuple[2]}')
# # unpaking the tuple 
# ten , *twenty_to_forty ,fifty = mytuple 

# print(ten)
# print(twenty_to_forty)
# print(fifty)

# 3. Write a Python program to check if a given number is positive, negative, or zero using if-else.
# user_input = int(input('Enter you num:'))
# if user_input < 0:
#     print('number is negative')
# elif user_input == 0:
#     print('number is zero')
# elif user_input > 0:
#     print('number is postive')
# else: 
#     print(f'{user_input} is not allow!')
# Given a set:
# fruits = {"apple", "banana", "cherry"}
# Add "mango" to the set.


# fruits = {"apple", "banana", "cherry"}
# fruits.add('mango')
# print(f'After adding mango in the fruits {fruits}')
# # Remove "banana" safely without error.
# fruits.discard('banana')
# print(f'After removing the banana in the fruits {fruits}')
# # Check if "grapes" exists in the set and print 
# if 'grapes' in fruits:
#     print('grapes in the fruits')
# # "Found" if true, otherwise "Not Found".
# else:
#     print('Not Found')

# 4. Write a Python program to reverse a given string without using built-in functions.

# def reverse_str(strr):
#     return strr[::-1]

# print(reverse_str("hello"))

# 5. Create a Python function that takes a list of numbers and returns the sum of only even numbers.
# def even_list(even_list):
#     new_list = [item for item in even_list if item % 2 == 0]
#     # new_list = []
#     # for item in even_list:
#     #     if item % 2 == 0:
#     #         new_list.append(item)
#     return new_list
# mylist = [1,2,3,4,5,6,7,8]
# print(even_list(mylist))

# # Given two tuples:
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# # Merge them into a single tuple.
# single_tuple = t1 + t2
# print(single_tuple)

# 6. Write a Python program to remove duplicates from a given list without using set().

# Given two dictionaries:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# # Merge both dictionaries into one.
# merge_dict = dict1 | dict2
# print(merge_dict)

# 7. Write a Python program to count how many times each element appears in the list:
# items = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# count_dict = {}
# for item in items:
#     count_dict[item] = count_dict.get(item,0) + 1
# print(count_dict)

# Given a list:
# lst = [10, 20, 30, 40]

# Convert it into a tuple and print its type.
# covt_into_tuple = tuple(lst)
# print(covt_into_tuple)
# print(type(covt_into_tuple))

# 8. Write a Python program to take a user-inputted number and check if it is prime or not.
# user_input = int(input('Enter the prime num:'))
# if user_input % 2 != 0 and user_input >= 2 and user_input > 0:
#     print(f'{user_input} is prime number')
# elif user_input % 2 == 0:
#     print(f'{user_input} is not prime number')


# Given a nested dictionary:
# data = {"student1": {"name": "Ali", "marks": 80}, "student2": {"name": "Sara", "marks": 90}}
# # Print Sara's marks using dictionary indexing.
# data['student2']['name'] = "Sara's"

# print(f"After changing Sara to Sara's dict is {data}
# ")

# 9. Write a Python program that prints numbers from 1 to 20 but skips multiples of 3 using a loop.
# for i in range(1,21):
#     if i % 3 == 0:
#         continue
#     print(i,end=' ')


# Given a string:
# text = "hello world"
# # Capitalize only the first letter of each word without using title().
# capitalize_letter = ' '.join(word[0].upper() + word[1:] if word else '' for word in text.split())

# print(capitalize_letter)

# print(f'Capitalize only the first letter of {text} is {text.title()}')


# 10. Write a Python function that takes a list of numbers and returns the second-largest number.

# def sec_last_num_of_list(listOfNumbers):
#     return listOfNumbers[-2]

# lst = [1,2,3,4,5,76,4,2,1]
# print(f'The second last item of the {lst} is {sec_last_num_of_list(lst)}')

# 11. Create a Python infinite loop that prints "Running..." but stops when the user inputs "exit".

# def infinite_loop():
#     while True:
#         print('Running.......')
#         if input("Type 'exit' to stop").lower() == 'exit':
#             break
# infinite_loop()

# Star Pattern Questions ⭐
# 1. Write a Python program to print the following right-angled triangle pattern:
# *
# **
# ***
# ****
# num = int(input('enter the num:'))
# for i in range(0,num+1):
#     print('*' * i)

# 2. Modify the above program to print the triangle in reverse order:
# *****
# ****
# ***
# **
# *

# n = int(input('Enter the row of stars you want to print :'))
# for i in range(n,0,-1):
#     print('*' * i)

# 3. Write a Python program to print a left-aligned pyramid:
#     *
#    **
#   ***
#  ****
# *****

# n = int(input('enter the row of stars you want to print left-aligned:'))
# for i in range(1,n+1):
#     print(' ' * (n-i) + '*' * i )

# 4. Modify the above program to print an inverted left-aligned pyramid:
# *****
#  ****
#   ***
#    **
#     *
# n = int(input('Enter the row of the stars you want:'))
# for i in range (n , 0 ,-1):
#     print(" " * (n-i) + '*' * i)

# 5. Write a Python program to print a diamond pattern:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
n = int(input('Enter the row to dimond:'))
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))































