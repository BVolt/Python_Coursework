"""
Class: 2520.01
Authors: Brenden Johnson
Assignment: Lab #2
Completed: 2/05/2023
"""

# Task 1
PV = float(input("Enter the present value: "))
INT = float(input("Enter the interest percentage: "))
YRS = int(input("Enter the years: "))
FV = PV * (1 + INT/100)**YRS
print("Future value is %.2f" % FV)

'''
Output

Enter the present value: 1000.0
Enter the interest percentage: 5.0
Enter the years: 30
Future value is 4321.94

Enter the present value: 1530.50
Enter the interest percentage: 3.5
Enter the years: 15
Future value is 2564.12
'''

# Task 2a
v1, v2, v3 = int(5), int(2), int(1)
v1 += 1
v2 -= 1
v3 += v1 * v2
print("v1: %d" % v1, "\nv2: %d" % v2, "\nv3: %d" % v3)

'''
Output

v1: 6 
v2: 1 
v3: 7
'''

# Task 2b
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
first, second, third = second, third, first
print("After Swap...\nfirst: %d" % first, "\nsecond: %d" % second, "\nthird: %d" % third)

'''
Output

Enter first number: 5
Enter second number: 7
Enter third number: 2
After Swap...
first: 7 
second: 2 
third: 5
'''


# Task 3
print("Enter the value of num1 and num2")
num1 = int(input())  # I elected to make the python code identical in output to the java
num2 = int(input())  # code, although I could've put the prompt in each input() function.
quotient = num1/num2
remainder = num1 % num2
print("Quotient when %d" % num1, "/ %d" % num2, "is: %d" % quotient)
print("Remainder when %d" % num1, "is divided by %d" % num2, "is: %d" % remainder)

'''
Output

Enter the value of num1 and num2
12
35
Quotient when 12 / 35 is: 0
Remainder when 12 is divided by 35 is: 12

Enter the value of num1 and num2
35
13
Quotient when 35 / 13 is: 2
Remainder when 35 is divided by 13 is: 9

'''