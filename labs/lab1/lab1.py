"""
Name: Evie Fleischman
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)

calc_area()

def calc_rec_area():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area = length * width
    print("Area =", area)

calc_rec_area()

def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height

calc_volume()

def shooting_percentage():
    shotsmade = eval(input("Enter the Shots Made:"))
    totalshots = eval(input("Enter Total Shots Taken:"))
    shotpercent = ((shotsmade/totalshots) * 100)

shooting_percentage()

def coffee():
    poundscoffee = eval(input("Enter Number of Pounds of Coffee Purchased:"))
    totalorder = (poundscoffee * 10.50) + (poundscoffee * .86) + 1.50

    coffee()

def kilometers_to_miles():
    johnkilo = eval(input("Enter Number of Kilometers Traveled"))
    converstion = (johnkilo/1.61)