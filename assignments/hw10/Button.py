"""
Name: evie fleischman
Button.py

Problem: This program creates the class, "Button" to create a game shown in three_door_game.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
        self.label = Text(Point(shape.getWidth/2, shape.getHeight/2), self.label)

    def get_label(self):
        return self.label

    def draw(self, win):
        win = GraphWin("Three Door Game", win.getWidth(), win.getHeight())

        self.shape.draw(win)
        self.label.draw(win)

    def undraw(self, win):
        self.shape.undraw(win)
        self.label.undraw(win)

    def is_clicked(self, point):
        if self.shape.getP1.getX() < point.getX() < self.shape.getP2.getX():
            if self.shape.getP1.getY() > point.getY() > self.shape.getP2.getY():
                return True
            else:
                return False
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.label.setText(label)
