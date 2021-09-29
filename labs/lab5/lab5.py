"""
Name: evie fleischman
lab5.py
"""

import math
from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target




    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on Three Points")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)
    # and display its area in the graphics window.

    # distance
    dx_ab = p1.getX() - p2.getX()
    dy_ab = p2.getY() - p1.getY()

    length_ab = (dx_ab**2) + (dy_ab**2)
    length_ab = math.sqrt(length_ab)

    dx_bc = p2.getX() - p3.getX()
    dy_bc = p3.getY() - p2.getY()

    length_bc = (dx_bc**2) + (dy_bc**2)
    length_bc = math.sqrt(length_bc)

    dx_ac = p1.getX() - p3.getX()
    dy_ac = p3.getY() - p1.getY()

    length_ac = (dx_ac ** 2) + (dy_ac ** 2)
    length_ac = math.sqrt(length_ac)
    perimeter = length_ab + length_bc + length_ac
    perimeter_txt = Text(Point(5, 4), "The perimeter equals: " + str(perimeter))
    perimeter_txt.draw(win)
    # area
    s = perimeter/2
    area = s * ((s-length_ab)*(s-length_bc)*(s-length_ac))
    math.sqrt(area)

    area_txt = Text(Point(5, 2), "The area is: " + str(area))
    area_txt.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's centern
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_box = Entry(Point(win_width / 2 - 50, win_height / 2 + 40), 5)
    red_box.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_box = Entry(Point(win_width / 2 - 50, win_height / 2 + 70), 5)
    green_box.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_box = Entry(Point(win_width / 2 - 50, win_height / 2 + 100), 5)
    blue_box.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())

        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to exit")
    win.getMouse()
    win.close()
    win.getMouse()
    win.close()

def process_string():
    s = eval(input("Enter a message: "))
    print(s[0])
    print(s[-1])
    print(s[2:6])
    print(s[0] + s[-1])
    print(s[0:3] * 10)
    for i in range(len(s)):
        c = s[i]
        print(c)
    print(len(s))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1]+values[3]
    print(x)
    x = values[0]+values[2]
    print(x)
    x = values[1]*5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    acc = 0
    series = eval(input("Enter the number of terms: "))

    for i in range(series):
        i = 2 + 2 * (i % 3)
        acc = acc + series
        print(i, end=" ")
        acc += i
    print("sum = " + str(acc))


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()

    pass


main()
