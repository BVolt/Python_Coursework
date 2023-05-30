"""
Assignment: Project 4
Author: Brenden Johnson
Due: 4-6-2023
Course: 2520.01
"""
import turtle


class Pair:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        print("<{x}, {y}>".format(x = self.x, y = self.y))

    
    def __add__(self, p):
        return Pair(self.x + p.x, self.y + p.y)
    
    def __mul__(self, p):
        return Pair(self.x * p.x, self.y * p.y)
    
    def __truediv__(self, p):
        return Pair(self.x * self.y - p.x * p.y, self.x * p.x - self.y * p.y)



def task1main():

    # Test Run 1 Vars
    p1 = Pair(3, 2)
    p2 = Pair(1, 5)
    p3 = Pair(4, 3)

    # Test Run 2 Vars
    # p1 = Pair(2, 9)
    # p2 = Pair(7, 20)
    # p3 = Pair(400, 2)

    print("Starting Pairs:")
    p1.__str__()
    p2.__str__()
    p3.__str__()

    print("\nBeginning Operations...\n")
    print("Pair 1 + Pair 2:")
    (p1 + p2).__str__()
    print("Pair 1 * Pair 2:")
    (p1 * p2).__str__()
    print("Pair 1 / Pair 2:")
    (p1 / p2).__str__()
    print("Pair 1 + Pair 2 * Pair 3:")
    (p1 + p2 * p3).__str__()
    print("Pair 1 * Pair 2 / Pair 3 + Pair 1:")
    (p1 * p2 / p3 + p1).__str__()



task1main()

'''
Output


# Test Run 1

Starting Pairs:
<3, 2>
<1, 5>
<4, 3>

Beginning Operations...

Pair 1 + Pair 2:
<4, 7>
Pair 1 * Pair 2:
<3, 10>
Pair 1 / Pair 2:
<1, -7>
Pair 1 + Pair 2 * Pair 3:
<7, 17>
Pair 1 * Pair 2 / Pair 3 + Pair 1:
<21, -16>


# Test Run 2

Starting Pairs:
<2, 9>
<7, 20>
<400, 2>

Beginning Operations...

Pair 1 + Pair 2:
<9, 29>
Pair 1 * Pair 2:
<14, 180>
Pair 1 / Pair 2:
<-122, -166>
Pair 1 + Pair 2 * Pair 3:
<2802, 49>
Pair 1 * Pair 2 / Pair 3 + Pair 1:
<1722, 5249>
'''

SCALE_FACTOR = 10

class Polygon:
    def __init__(self, pointList=[]):
        self.__pointList = pointList

    def addPoint(self, point):
        self.__pointList.append(point)

    def getPoint(self, index):
        return self.__pointList[index]

    def displaySide(self):
        return len(self.__pointList)

    def draw(self):
        scaled_points = [(x * SCALE_FACTOR, y * SCALE_FACTOR) for x, y in self.__pointList]
        turtle.penup()
        turtle.goto(scaled_points[0])
        turtle.pendown()

        for point in scaled_points[1:]:
            turtle.goto(point)

        turtle.goto(scaled_points[0])
        turtle.done()

class Rectangular(Polygon):
    def __init__(self, lower_left, upper_right):
        self.__lower_left = lower_left
        self.__upper_right = upper_right
        lower_right = (self.__upper_right[0], self.__lower_left[1])
        upper_left = (self.__lower_left[0], self.__upper_right[1])
        super().__init__([self.__lower_left, upper_left, self.__upper_right, lower_right])

    def getLowerLeft(self):
        return self.__lower_left

    def getUpperRight(self):
        return self.__upper_right

def task2main():
    pentagon = Polygon([(0, 0), (0, 5), (3, 8), (6, 5), (6, 0)])
    print("Pentagon sides:", pentagon.displaySide())
    pentagon.draw()

    turtle.TurtleScreen._RUNNING = True

    rectangle = Rectangular((0, 0), (5, 5))
    print("Rectangle LowerLeft:", rectangle.getLowerLeft())
    print("Rectangle UpperRight:", rectangle.getUpperRight())
    print("Rectangle sides:", rectangle.displaySide())
    rectangle.draw()


task2main()

'''
Output

Pentagon sides: 5
Rectangle LowerLeft: (0, 0)
Rectangle UpperRight: (5, 5)
Rectangle sides: 4
'''