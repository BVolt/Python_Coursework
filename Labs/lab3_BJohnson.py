"""
Author: Brenden Johnson
Assignment: Lab 3
Class: 2520.01
Completed: 2/08/2023
"""


# Task 1
print("Find the max of three values")
test_case = int(input("Enter 1 for strings, 2 for integers, 3 for floats: "))
if test_case == 1:
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    third = input("Enter third string: ")
elif test_case == 2:
    first = int(input("Enter first integer: "))
    second = int(input("Enter second integer: "))
    third = int(input("Enter third integer: "))
else:
    first = float(input("Enter first float: "))
    second = float(input("Enter second float: "))
    third = float(input("Enter third float: "))
print("Max value is:", max(first, second, third))

'''
Output

Test Run #1

Find the max of three values
Enter 1 for strings, 2 for integers, 3 for floats: 1
Enter first string: hello
Enter second string: how're you
Enter third string: hoho
Max value is: how're you

Test Run #2
Find the max of three values
Enter 1 for strings, 2 for integers, 3 for floats: 2
Enter first integer: 420
Enter second integer: 351
Enter third integer: 530
Max value is: 530

Test Run #3
Find the max of three values
Enter 1 for strings, 2 for integers, 3 for floats: 3
Enter first float: -35.8
Enter second float: -28
Enter third float: -36.5
Max value is: -28.0
'''

# Task2
count = int(input("Please enter the number of items purchased: "))
total = int(input("Please enter the total cost: "))
print("Average=", 0 if count == 0 else total/count)

'''
Output

Test Run #1

Please enter the number of items purchased: 5
Please enter the total cost: 300
Average= 60.0

Test Run #2

Please enter the number of items purchased: 0
Please enter the total cost: 300
Average= 0
'''

# Task 3(a)
j=1
while j < 10 :
      j += 2
      if j == 5 :
            continue
      print(j, end =  " ")


'''
Predicted Output
(a)
3
5
7
9
11

Actual Output
(b) 3 7 9 11 

Reflections
(c) Did not guess the same.
Clearly the continue skips the print statement 
and end =" " stops newline.
'''


# Task 3(b)
for j in range(50):
      j += 2
      print(j, end=" ")
      if j == 15:
            break

'''
Predicted Output
(a) 3 5 7 9 11 13 15

Actual Output
(b) 2 3 4 5 6 7 8 9 10 11 12 13 14 15 

Reflections
(c) Did not guess the same.
its clear that the j begins at zero 
and only adds two once.
'''

# Task 4
number = int(input("Enter a number to check Prime or Not: "))
i, count = int(2), int(0)
while i <= number/2:
    if number % i == 0:
        count += 1
        break
    i += 1
if count == 0:
    print(number, "is prime number")
else:
    print(number, "is not a prime number")

'''
Output

Test Run #1

Enter a number to check Prime or Not: 71
71 is prime number

Test Run #2

Enter a number to check Prime or Not: 119
119 is not a prime number

Test Run #3

Enter a number to check Prime or Not: 11
11 is prime number

Test Run #4

Enter a number to check Prime or Not: 12
12 is not a prime number

Test Run #5

Enter a number to check Prime or Not: 1
1 is prime number
'''