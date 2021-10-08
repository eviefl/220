"""
Name: evie fleischman
greeting.py

Problem:This program displays a greeting card, solving the problem of someone not knowing it is
Valentine's Day, because why would they it's October lol.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*
import time


def main():

    # graphics window
    width = 400
    height = 400
    win = GraphWin("Greeting Card", width, height)
    win.setBackground("lightcoral")

    # text 1
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Happy Valentine's Day!")
    instructions.draw(win)
    instructions.setTextColor("maroon")

    # top of heart ( <3 )
    shape = Circle(Point(138, 100), 60)
    shape.setOutline("maroon")
    shape.draw(win)

    shape = Circle(Point(257, 100), 60)
    shape.setOutline("maroon")
    shape.draw(win)

    # rectangle to cover circles
    r = Rectangle(Point(50, 170), Point(350, 100))
    r.setFill("lightcoral")
    r.setOutline("lightcoral")
    r.draw(win)

    # arrow line
    pt_x = 25
    pt_y = 370
    arrow_line = Line(Point(pt_x, pt_y), Point(pt_x + 100, pt_y - 100))
    arrow_line.setFill("white")
    arrow_line.setOutline("white")
    arrow_line.draw(win)

    # arrow top
    arrow_head = Polygon(Point(pt_x + 100, pt_y - 100), Point(pt_x + 80, pt_y - 90), Point(pt_x + 90, pt_y - 80))
    arrow_head.setOutline("white")
    arrow_head.setFill("burlywood")
    arrow_head.draw(win)

    # arrow bottom
    arrow_end = Polygon(Point(pt_x + 20, pt_y - 20), Point(pt_x + 5, pt_y - 5), Point(pt_x + 15, pt_y - 5))
    arrow_end.setFill("burlywood")
    arrow_end.setOutline("white")
    arrow_end.draw(win)

    arrow_end_two = Polygon(Point(pt_x + 20, pt_y - 20), Point(pt_x + 5, pt_y - 5), Point(pt_x + 5, pt_y - 15))
    arrow_end_two.setFill("burlywood")
    arrow_end_two.setOutline("white")
    arrow_end_two.draw(win)

    # bottom of heart ( <3 )
    line_one = Line(Point(90, 170), Point(200, 360))
    line_one.setFill("maroon")
    line_one.setOutline("maroon")
    line_one.draw(win)

    line_two = Line(Point(310, 170), Point(200, 360))
    line_two.setFill("maroon")
    line_two.setOutline("maroon")
    line_two.draw(win)

    # makes arrow move    >> I was just trying things and I'm unsure of why this works. I guessed 400 because that is the width of my screen.
    for i in range(400):
        arrow_head.move(1, -1)
        arrow_line.move(1, -1)
        arrow_end.move(1, -1)
        arrow_end_two.move(1, -1)
        time.sleep(.01)

    # text two
    instructions.undraw()
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click anywhere to close")
    instructions.draw(win)

    # close after mouse click
    win.getMouse()
    win.close()


main()
