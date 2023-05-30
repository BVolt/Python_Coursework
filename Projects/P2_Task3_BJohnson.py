"""
Author: Brenden Johnson
Assignment: Project 3 - Task 3
Date: 3-2-2023
Course: 2520.01
"""

#Task 3
import turtle



def encodeZip():
    zipString = input("Enter Zip Code in XXXXX-XXXX format: ")
    zipString = zipString.replace("-", "")
    sum = 0
    for char in zipString:
        sum += int(char)
    checkSum = 10 - (sum % 10)
    zipString += str(checkSum)
    return zipString

def drawBarcode(t, zipCode):
    draw1Bar(t)
    for char in zipCode:
        drawDigit(t, digitsToBinary[int(char)])
    draw1Bar(t)


def drawDigit(t, binArray):
    for number in binArray:
        if number == 0:
            draw0Bar(t)
        elif number == 1:
            draw1Bar(t)


def draw0Bar(t):
    t.forward(6)
    t.penup()
    t.backward(6)
    t.right(90)
    t.forward(6)
    t.left(90)
    t.pendown()

def draw1Bar(t):
    t.forward(14)
    t.penup()
    t.backward(14)
    t.right(90)
    t.forward(6)
    t.left(90)
    t.down()

def main():
    zipCode = encodeZip()  # Encode Zip Code

    # Initialize turtle window
    t = turtle.Turtle()
    t.speed('fastest')
    t.pensize(2)
    t.left(90)

    # Draw Barcode
    drawBarcode(t, zipCode)
    turtle.done()


if __name__ == "__main__":
    digitsToBinary = \
        [[1, 1, 0, 0, 0],  # '0'
         [0, 0, 0, 1, 1],  # '1'
         [0, 0, 1, 0, 1],  # '2'
         [0, 0, 1, 1, 0],  # '3'
         [0, 1, 0, 0, 1],  # '4'
         [0, 1, 0, 1, 0],  # '5'
         [0, 1, 1, 0, 0],  # '6'
         [1, 0, 0, 0, 1],  # '7'
         [1, 0, 0, 1, 0],  # '8'
         [1, 0, 1, 0, 0],  # '9'
         ]
    main()

'''
Results
bar codes in pdf

Test 1
Enter Zip Code in XXXXX-XXXX format: 55555-1237

Test 2
Enter Zip Code in XXXXX-XXXX format: 91768-1111

Test 3
Enter Zip Code in XXXXX-XXXX format: 928001-1212

'''