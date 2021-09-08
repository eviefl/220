"""
Name: evie fleischman
lab2.py
"""
import math

def sum_of_threes():
    bound = eval(input("enter a number:"))
    total = 0
    for x in range(0, bound+1, 3):
        total = total + x
    print(total)


sum_of_threes()


def multiplication_table():
    for height in range(1, 11):
        for length in range(1, 11):
            print(height*length)
            print()


multiplication_table()


def triangle_area():
    sidea = eval(input("enter value of side a:"))
    sideb = eval(input("enter value of side b:"))
    sidec = eval(input("enter value of side c:"))
    s = (sidea+sideb+sidec)/2
    area = math.sqrt(s*(s-sidea)*(s-sideb)*(s-sidec))
    print(area)


triangle_area()


def sumSquares():
    num1 = eval(input("enter starting number:"))
    num2 = eval(input("enter ending number"))
    acc = 0
    for x in range(num1, num2 + 1):
        acc = acc + x**2
    print(acc)


sumSquares()


def power():
    base = eval(input("enter base number:"))
    exponent = eval(input("enter an exponent:"))
    amount = 1
    for i in range(exponent):
        amount = amount * base
        print(amount)
power()

