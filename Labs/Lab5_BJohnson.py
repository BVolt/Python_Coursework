"""
Author: Brenden Johnson
Assignment: Lab 5
Course: 2520.01
Date: 2-28-2023
"""
import turtle


def main():
    turtle.color('yellow', 'orange')  # Drawing Colors
    turtle.Screen().setup(1000, 700)  # Initial Size
    turtle.Screen().bgcolor('black')  # Background Color
    turtle.width(2)  # Drawing Width
    turtle.speed(100)  # Draw speed

    # Drawing Loop
    p = 0
    for i in range(1, 244):
        # Turns for Spiral
        turtle.forward(2 + i / 4)
        turtle.left(30 - i / 12)
        if i % 50 == 0 or i == 243:
            p += 1  # Multiplier for flower size
            turtle.begin_fill()  # Setup flower to be filled in
            for j in range(10):  # Creates 10 circles
                turtle.circle(p * 10)
                turtle.right(36)  # Turn by 36 degrees
            turtle.end_fill()  # Fill flower on completion
        # Draw first flower smaller
        if i == 1:
            print(p)
            turtle.begin_fill()
            for j in range(10):
                turtle.circle(5)
                turtle.right(36)
            turtle.end_fill()

    turtle.done()


if __name__ == "__main__":
    main()
