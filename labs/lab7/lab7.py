"""
Name: evie fleischman
Partner: <your partner's name goes here – first and last>
lab7.py
"""

import math


def cash_conversion():
    user_int = eval(input("enter an integer: "))
    print("$", '{:.2f}'.format(user_int))


def encode():
    acc = ""
    message = input("enter message: ")
    key_input = eval(input("enter key: "))
    for i in message:
        new_chr = key_input + ord(i)
        new_chr = chr(new_chr)
        acc = acc+new_chr
    return acc


def sphere_area(radius):
    sph_area = 4 * math.pi * (radius**2)
    return sph_area


def sphere_volume(radius):
    sph_vol = (4/3) * math.pi * (radius**3)
    return sph_vol


def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + (i**3)
    return acc


def encode_better():
    acc = ""
    s = input("enter message: ")
    k = input("enter key: ")
    for i in range(len(s)):
        c = s[i]
        key = k[i]
        key = ord(key) - 97
        new_chr = key + ord(c)
        new_chr = chr(new_chr)
        acc = acc + new_chr
    return acc


def main():
    # add function calls here

    print(sphere_area(7))
    print(sphere_volume(7))
    print(sum_n(7))
    print(sum_n_cubes(7))
    cash_conversion()
    encode()
    encode_better()
    pass


main()
