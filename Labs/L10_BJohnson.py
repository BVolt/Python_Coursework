"""
Assignment: Lab 10
Author: Brenden Johnson
Due: 4-26-2023
Course: 2520.01
"""

# Task 1
class Bicycle:
    def __init__(self, gear0, speed0):
        self.gear = gear0
        self.speed = speed0

    def applyBrake(self, decrement):
        self.speed -= decrement

    def speedUp(self, increment):
        self.speed += increment

    def toString(self):
        return "No of gears are {gear}\nspeed pf bicycle is {speed}".format(gear = self.gear, speed = self.speed)


class MountainBike(Bicycle):
    def __init__(self, gear, speed, startHeight):
        super(MountainBike, self).__init__(gear, speed)
        self.seatHeight = startHeight

    def setHeight(self, newValue):
        self.seatHeight = newValue

    def toString(self):
        return Bicycle.toString(self) + "\nseat height is {seatHeight}".format(seatHeight = self.seatHeight)


def task1main():
    mb = MountainBike(3, 100, 25)
    print(mb.toString())


task1main()

'''
Output

No of gears are 3
speed pf bicycle is 100
seat height is 25
'''


# Task 2
class Fraction:
    def __init__(self, n = 0, d = 1):
        self.__num = n
        self.__den = d

    def __add__(self, f):
        return Fraction(self.__num * f.__den + self.__den * f.__num, self.__den * f.__den)

    def __mul__(self, f):
        return Fraction(self.__num * f.__num, self.__den * f.__den)

    def __eq__(self, f):
        return self.__num*f.__den == self.__den*f.__num

    def display(self):
        print("{num}/{den}".format(num = self.__num, den = self.__den))


def task2main():
    f1 = Fraction(3, 7);
    f2 = Fraction(2, 5);
    f3 = Fraction(1, 3);
    f4 = Fraction(2, 6);
    result = f1 + f2 * f3;
    result.display()
    if f1 == f3:
        print("f1 and f3 are the same")
    else:
        print("f1 and f3 not equal")
    if f3 == f4:
        print("f3 and f4 are the same")
    else:
        print("f3 and f4 not equal")
    return 0;


task2main()

'''
Output

59/105
f1 and f3 not equal
f3 and f4 are the same
'''