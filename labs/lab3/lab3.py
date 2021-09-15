"""
Name: evie fleischman
lab3.py
"""


def function():
    acc = 0
    grades = eval(input("Enter the number of grades:"))
    for i in range(grades):
        homework = eval(input("Enter your grade on HW " + str(i) + ": "))
        acc = acc + homework
    print(acc/grades)


function()


def tip_jar():
    total = 0
    for i in range(5):
        people = eval(input("Enter the amount put into jar: $"))
        total = total + people
    print(total)


tip_jar()


def newton():
    x = eval(input("Enter a number:"))
    x_amount = eval(input("Enter how many times to run approximation:"))
    approx = x/2
    for x in range(x_amount):
        approx = (approx + (x/approx)) / 2
    print(approx)


newton()


def sequence():
    terms = eval(input("Enter the number of terms: "))
    for y in range(1, 1 + terms):
        print(1 + (y // 2 * 2))


sequence()


def pi():
    acc = 1
    terms = eval(input("Enter the number of terms: "))
    for n in range(terms):
        num = 2 + (n//2 * 2)
        denom = 1 + ((n + 1) // 2 * 2)
        acc = acc * (num/denom)
    print(acc * 2)


pi()
