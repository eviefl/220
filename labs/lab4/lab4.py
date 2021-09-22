"""
Name: evie fleischman
lab4.py
"""
import math
from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    # shape = Circle(Point(50, 50), 20)
    # shape.setOutline("red")
    # shape.setFill("red")
    # shape.draw(win)

    # builds a rectangle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        # makes new rectangles
        shape = Rectangle(Point(p.getX()-10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - p.getX()
        dy = p.getY() - p.getY()
        shape.move(dx, dy)

    instructions.undraw()
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to Quit")
    instructions.draw(win)

    win.getMouse()
    win.close()

squares()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    width = 400
    height = 400

    win = GraphWin("Rectangle", width, height)

    p = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p, p2)
    r.draw(win)
    length = p2.getY() - p.getY()
    wid = p2.getX() - p.getX()
    area = abs(length*width)
    perimeter = abs(2 * (length + wid))
    instructions = Text(Point(width / 2, height - 50), "The area is: " + str(area))
    instructions.draw(win)
    instructions = Text(Point(width / 2, height - 30), "The perimeter is: " + str(perimeter))
    instructions.draw(win)
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to End Program")
    instructions.draw(win)
    win.getMouse()
    win.close()


rectangle()


def circle():
    width = 400
    height = 400

    win = GraphWin("Circle", width, height)

    c1 = win.getMouse()
    c2 = win.getMouse()

    radius_distance = ((c2.getX() - c1.getX())**2) + ((c2.getY() - c1.getY())**2)
    radius_distance = math.sqrt(radius_distance)

    c = Circle(c1, radius_distance)
    c.draw(win)

    instructions = Text(Point(width / 2, height - 40), "The radius is: " + str(radius_distance))
    instructions.draw(win)
    instructions = Text(Point(width/2, height-10), "Click to End Program")
    instructions.draw(win)

    win.getMouse()
    win.close()


circle()


def pi2():
    acc = 0
    n = eval(input("enter how many times you would like to run the program: "))
    for i in range(n):
        num = 4
        denom = 1 + 2 * i
        output = (num/denom) * ((-1) * i)

    print(math.pi - acc)


pi2()
