"""
Name: evie fleischman
bumper.py

Problem: This program represents bumper cars.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import*

# draw screen
# draw circles
# make circle move
# print something to detect when the circle hits the edge (just for me)
# now try to get the circle to reflect back when it gets to edge
# when it gets to the other side, use same logic to make it reflect again, now up and down?
# get circle to bound around sides (random)
# now introduce second circle, using same logic
# print something to detect when circles touch (just for me)
# now program to where the circles bounce off each other when they cross paths.
# use while loop


def circles():
    # graphics window
    width = 400
    height = 400
    win = GraphWin("Bumper", width, height)
    win.setBackground("olive")

    # circle_one
    pt_one = width/2
    pt_two = height/2
    circle_one = Circle(Point(pt_one, pt_two), 30)
    circle_one.setFill("gold")
    circle_one.draw(win)

    # circle two
    circle_two = Circle(Point(pt_one, pt_two), 30)
    circle_two.setFill("honeydew")
    circle_two.draw(win)

    # dx =
    # dy =
    # while



    win.getMouse()
    win.close()


def get_random(move_amount):
    move_amount = int(move_amount)
    return randint(-move_amount, move_amount)


def did_collide(circle_one, circle_two):
    center_one = circle_one.getCenter()
    center_two = circle_two.getCenter()
    radius_one = circle_one.getRadius()
    radius_two = circle_two.getRadius()
    if (center_one + radius_one) == (center_two - radius_two):
        return True


def hit_vertical(circle_one, win):
    if circle_one <= win:
        return True
    else:
        return False


def hit_horizontal(circle_one, win):
    if circle_one <= win:
        return True
    else:
        return False


# def get_random_color():



def main():
    circles()
    get_random(5)
    did_collide()
    hit_vertical()
    hit_horizontal()
    get_random_color()


main()
