"""
Author: Brenden Johnson
Assignment: Lab 4
Class: 2520.01
Date: 2/19/2023
"""
import math

# Task 1
print("sum =", sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print("fsum =", math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

'''
Output

sum = 0.9999999999999999
fsum = 1.0

Discussion
From the results it appears the fsum has a higher level of precision
than sum because the correct answer should be 1.0
'''

# Task 2
def task2():
    for i in range(8):
        print(i, end='')


print(task2())

'''
Output

01234567None

Discussion
It is clear that if the function does not have a return value
the function will instead return none.
'''

# Task 3
#3(a)
def fun (x = 1, y = 2, z):
    z = x + y
    y += 1
    return z*y
print(fun(3, z= 5))

#3(b)
def hoho (x, y = 2, z = 1):
    z = x + z
    y += 1
    return z*y
print(hoho(5), hoho(6, z = 3, y = 1))

'''
Discussion 

3(a) does have an error because z is a non default argument
and must be defined before the default arguments

3(b) does not have an error because the non default argument
x is in the right location. So the output is as follows:

Output
18 18
'''

# Task 4
def main():
    x, y = input("Enter first value: "), input("Enter second value: ")
    x, y = swap(x, y)
    print("The swapped values are: ", x, y)
def swap(a, b):
    a, b = b, a
    return(a, b)
main()

'''
Output

Test Run 1
Enter first value: 3
Enter second value: 4
The swapped values are:  4 3

Test Run 2
Enter first value: 9
Enter second value: 40
The swapped values are:  40 9

Discussion
The main() function does not reassign the values although the swap function
behaves as intended. So i rewrote the main to reassign and take input as well.
'''

# Task 5
a, b = 0, 5
def main():
    global a, b
    i = 10
    b = g(i)
    print(a + b + i)
def f(i):
    n = 0
    while n*n <= i:
        n = n + 1
    return n - 1
def g(a):
    b = 0
    for n in range(a):
        i = f(n)
        b = b + i
        return b
main()

'''
Discussion
a, b outside the function are globally scoped. The a and b inside main is also
global because of the global keyword. i and b in main are locally scoped to main function.
n in the f() function is local scope to f(). The b = 0 is locally scoped to g(a). The i and b 
are local scope to the for loop. Based on this the result should be as a would remain 0
i would remain 10 and b would return as 0.

Output
10
'''