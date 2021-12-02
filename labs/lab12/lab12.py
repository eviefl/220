"""
Name: evie fleischman
lab12.py
"""
from random import randint


def find_and_remove_first(list, value):
    ind = list.index(value)
    list.pop(ind)
    list.insert(ind, "Caty")
    print(list)


def good_input():
    num = eval(input("what is your value? "))
    while 1 > num or num > 10:
        if 1 > num:
            print("your value is too low")
        elif num > 10:
            print("your value is too high")
        num = eval(input("what is your value? "))
    else:
        return num


def num_digits():
    num = eval(input("what is your value? "))
    var = num
    while num > 0:
        val = 0
        var = num
        while num != 0:
            num = num // 10
            val += 1
        print(var, "has", val, "digits")
        num = eval(input("what is your value? "))
    print("your value is out of range")


def hi_lo_game():
    value = randint(0, 100)
    guesses = 1
    while guesses < 8:
        num = eval(input("what is your guess? "))
        if num > value:
            print("you are too high")
            guesses += 1
        elif num < value:
            print("you are too low")
            guesses += 1
        else:
            print("You win in", guesses, "guesses")
            return
    print("Sorry, you lose. The number was", value)


def main():
    find_and_remove_first([15, 20, 30, 40, 50], 30)
    read_data("read_data_test_data.txt")
    is_in_linear(12, [15, 20, 30, 40, 50])
    good_input()
    num_digits()
    hi_lo_game()


main()

