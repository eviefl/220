"""
Name: evie fleischman
vigenere.py

Problem: This program encodes a user's input using a user-inputted keyword.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*


def window():
    # creates window
    win_width = 400
    win_height = 400
    win = GraphWin("Vigenere", win_width, win_height)
    win.setBackground("white")

    # creates message entry box
    msg_text_pt = Point(win_width / 2 - 120, win_height / 2 - 140)
    msg_text = Text(msg_text_pt, "Message to Code: ")
    msg_box = Entry(Point(win_width / 2 + 50, win_height / 2 - 140), 20)
    msg_text.draw(win)
    msg_box.draw(win)

    # creates keyword entry box
    key_text_pt = Point(win_width / 2 - 120, win_height / 2 - 70)
    key_text = Text(key_text_pt, "Enter Keyword: ")
    key_box = Entry(Point(win_width / 2 + 50, win_height / 2 - 70), 20)
    key_text.draw(win)
    key_box.draw(win)

    # button
    rectangle = Rectangle(Point(win_width / 2 - 80, win_height / 2 + 100), Point(win_width / 2 + 80, win_height / 2 + 50))
    rectangle.draw(win)
    rectangle_text_pt = rectangle.getCenter()
    rectangle_text = Text(rectangle_text_pt, "Encode")
    rectangle_text.draw(win)

    # when user clicks on button
    user_click = win.getMouse()
    if rectangle.getP1().getX() <= user_click.getX() <= rectangle.getP2().getX() and rectangle.getP2().getY() <= user_click.getY() <= rectangle.getP1().getY():
        rectangle.undraw()
        message = msg_box.getText().upper().replace(" ", "")
        keyword = key_box.getText().upper().replace(" ", "")
        encode = code(message, keyword)
        rectangle_text.setText("Resulting Message: \n\n" + encode)
        message_pt = Point(win_width / 2, win_height / 2 + 180)
        message_text = Text(message_pt, "Click Anywhere to Close ")
        message_text.draw(win)

    # closes window after mouse click
    win.getMouse()
    win.close()


def code(message, keyword):
    acc = ""
    for i in range(len(message)):
        c = message[i]
        key = i % len(keyword)
        key = str(key)
        key = ord(key)
        new_chr = key + ord(c)
        new_chr = chr(new_chr)
        acc = acc + new_chr
    return acc


def main():
    window()


main()
