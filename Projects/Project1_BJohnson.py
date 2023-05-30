"""
Author: Brenden Johnson
Assignment: Project 1
Class: 2520.01
Completed: 2/15/2023
"""

import math


'''
#Task 1
print("Program to calculate BMI")
inp = int (input("Please enter a 1 for US system or 2 for Metric System: "))
if inp == 1:
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
elif inp == 2:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
if height <= 0 or weight <= 0:
    print("Invalid height or weight! Both must be above 0")
else:
    if inp == 1:
        BMI = 703 * (weight / height ** 2)
    elif inp == 2:
        BMI = (weight / height ** 2)
    print("Your Bmi is %.2f" % BMI)
    if BMI > 25:
        print("Your BMI indicates you are overweight")
    elif BMI < 18:
        print("Your BMI indicates you are underweight")
    else:
        print("You have a healthy BMI")
'''
'''
Output

Program to calculate BMI
Please enter a 1 for US system or 2 for Metric System: 1
Enter your weight in pounds: 155
Enter your height in inches: 70
Your Bmi is 22.24
You have a healthy BMI

Program to calculate BMI
Please enter a 1 for US system or 2 for Metric System: 1
Enter your weight in pounds: 172
Enter your height in inches: 68
Your Bmi is 26.15
Your BMI indicates you are overweight

Program to calculate BMI
Please enter a 1 for US system or 2 for Metric System: 2
Enter your weight in kilograms: 75
Enter your height in meters: 1.83
Your Bmi is 22.40
You have a healthy BMI

Program to calculate BMI
Please enter a 1 for US system or 2 for Metric System: 2
Enter your weight in kilograms: 51.5
Enter your height in meters: 1.68
Your Bmi is 18.25
You have a healthy BMI

Program to calculate BMI
Please enter a 1 for US system or 2 for Metric System: 1
Enter your weight in pounds: 300
Enter your height in inches: 65
Your Bmi is 49.92
Your BMI indicates you are overweight

Program to calculate BMI
Please enter a 1 for US system or 2 for Metric System: 2
Enter your weight in kilograms: 40
Enter your height in meters: 1.99
Your Bmi is 10.10
Your BMI indicates you are underweight

Program to calculate BMI
Please enter a 1 for US system or 2 for Metric System: 1
Enter your weight in pounds: 0
Enter your height in inches: 5
Invalid height or weight! Both must be above 0

Program to calculate BMI
Please enter a 1 for US system or 2 for Metric System: 2
Enter your weight in kilograms: 6
Enter your height in meters: 0
Invalid height or weight! Both must be above 0
'''




#Task 2
print("This program approximates the value of sin(x)")
inp = int(1)

while inp != 0:
    question = input("Would you like your test value in multiples of pi?\nEnter 'pi' for yes or 'no' for no: ")
    if question == "pi":
        numerator = float(input("Enter the numerator for your pi constant multiplier: "))
        denominator = float(input("Enter the denominator for your pi constant multiplier: "))
        x = (numerator/denominator) * math.pi
        print("\nTesting sin of", numerator, "/", denominator, "x pi...\n")
    elif question == "no":
        x = float(input("Please enter the value in radians you would like to test: "))
        print("\nTesting sin of", x, "...\n")
    else:
        x = float(input("Invalid input. Assuming Radians.\nPlease enter the value in radians you would like to test: "))
        print("\nTesting sin of", x, "...\n")
    sum = x
    term =x
    for i in range(1, 1000):
        term = (-1) * term * (x*x) / (2 * i * (2*i+1))
        sum += term

        if abs(sum - math.sin(x)) < .000001:
            break
    else:
        print("Sequence is not convergent after 1000 iteration")
    print("The estimated value", sum)
    print("Accurate Value", math.sin(x))
    print("The difference between the two is", sum-math.sin(x))
    inp = int(input("\nEnter a 1 to continue with tests or a 0 to terminate: "))

'''
Output

This program approximates the value of sin(x)
Would you like your test value in multiples of pi?
Enter 'pi' for yes or 'no' for no: pi
Enter the numerator for your pi constant multiplier: 1
Enter the denominator for your pi constant multiplier: 3

Testing sin of 1.0 / 3.0 x pi...

The estimated value 0.8660254450997811
Accurate Value 0.8660254037844386
The difference between the two is 4.131534248053015e-08

Enter a 1 to continue with tests or a 0 to terminate: 1
Would you like your test value in multiples of pi?
Enter 'pi' for yes or 'no' for no: pi
Enter the numerator for your pi constant multiplier: -1
Enter the denominator for your pi constant multiplier: 6

Testing sin of -1.0 / 6.0 x pi...

The estimated value -0.4999999918690232
Accurate Value -0.49999999999999994
The difference between the two is 8.130976725251315e-09

Enter a 1 to continue with tests or a 0 to terminate: 1
Would you like your test value in multiples of pi?
Enter 'pi' for yes or 'no' for no: no
Please enter the value in radians you would like to test: 0.112

Testing sin of 0.112 ...

The estimated value 0.11176584533333334
Accurate Value 0.11176599215128519
The difference between the two is -1.4681795185156332e-07

Enter a 1 to continue with tests or a 0 to terminate: 1
Would you like your test value in multiples of pi?
Enter 'pi' for yes or 'no' for no: pi
Enter the numerator for your pi constant multiplier: 1
Enter the denominator for your pi constant multiplier: 1

Testing sin of 1.0 / 1.0 x pi...

The estimated value -7.727858895155385e-07
Accurate Value 1.2246467991473532e-16
The difference between the two is -7.727858896380032e-07

Enter a 1 to continue with tests or a 0 to terminate: 1
Would you like your test value in multiples of pi?
Enter 'pi' for yes or 'no' for no: pi
Enter the numerator for your pi constant multiplier: 1
Enter the denominator for your pi constant multiplier: 2

Testing sin of 1.0 / 2.0 x pi...

The estimated value 0.999999943741051
Accurate Value 1.0
The difference between the two is -5.625894905492146e-08

Enter a 1 to continue with tests or a 0 to terminate: 1
Would you like your test value in multiples of pi?
Enter 'pi' for yes or 'no' for no: pi
Enter the numerator for your pi constant multiplier: 1
Enter the denominator for your pi constant multiplier: 4

Testing sin of 1.0 / 4.0 x pi...

The estimated value 0.7071064695751781
Accurate Value 0.7071067811865476
The difference between the two is -3.116113694856537e-07

Enter a 1 to continue with tests or a 0 to terminate: 1
Would you like your test value in multiples of pi?
Enter 'pi' for yes or 'no' for no: no
Please enter the value in radians you would like to test: 1.5

Testing sin of 1.5 ...

The estimated value 0.9974949556821353
Accurate Value 0.9974949866040544
The difference between the two is -3.092191913633968e-08

Enter a 1 to continue with tests or a 0 to terminate: 0
'''


