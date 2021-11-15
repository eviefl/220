"""
Name: evie fleischman
interest.py

Problem:
Certification of Authenticity:
I certify that this assignment is entirely my own work.

1. The program will output three different means (Root-mean-square, Harmonic, and Geometric) after the user in puts the number of values to be entered, and the user's inputed values.
2. Outputs: Root-mean-square average, the Harmonic Mean, and the Geometric Mean  Inputs: the number of values to be entered
3. The program must ask the user for the number of values to be entered, and then to enter those values,and the user's input should be run through the three different mean equations. Output should display on the screen the three different means (answers to equations) in the order of Root-mean-square, Harmonic mean, and Geometric mean, the number of values to be entered, and the user's entered numbers.
"""
import math

def main():
    user = eval(input("The Number of Values to Be Entered: "))
    for i in range(user):
        user_value = eval(input("Enter value: "))


main()
