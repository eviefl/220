"""
Name: evie fleischman
lab9.py
"""
from graphics import*
import math

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    infile_name = input("What is the file name? ")
    infile = open(infile_name, "r")
    outfile = open(infile_name + ".txt", "w")
    for line in infile:
        numbers = line.split()
        toNumbers(numbers)
        squareEach(numbers)
        sumList(numbers)
        outfile.write("Sum of Squares = ")


def starter():
    weight = float(input("enter weight: "))
    wins = int(input("enter wins: "))
    if weight >= 150 and weight < 160 and wins >= 5:
        print("You've earned a Starting Position.")
    elif weight > 199 or wins > 20:
        print("You've earned a starting position.")
    else:
        print("You've been rejected.")

def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year.")



def circleOverlap():
    win = GraphWin("Circles", 400, 400)
    # circle one
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle = Circle(p1, radius)
    circle.draw(win)

    # circle two
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius_two = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle_two = Circle(p1, radius)
    circle_two.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)

    if distance < radius + radius_two:
        print("The circles overlap. Click anywhere to close")
    else:
        print("The circles do not overlap. Click anywhere to close")

    win.getMouse()
    win.close()


def main():
    # add other function calls here

    nums = [5, 2, -1]
    addTen(nums)

    nums = [3, 5.7, 7]
    squareEach(nums)

    sumList(nums)

    strList = ["3", "5.7", "2"]
    toNumbers(strList)

    writeSumOfSquares()

    starter()

    leapYear(2000)

    circleOverlap()

    pass


main()
