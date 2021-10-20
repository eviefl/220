"""
Name: evie fleischman
lab8.py
"""
from lab7 import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    i = 1
    for line in infile:
        new_line = line.split()
        for word in new_line:
            outfile.write(str(i) + " " + word + "\n")
            i = i + 1


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        outfile.write(" ".join(new_line) + "\n")


def calc_check_sum(isbn):
    acc = 0
    isbn = str(isbn)
    for i in range(len(isbn)):
        num = int(isbn * (10-i))
        acc += num
    return acc % 11


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        outfile.write(line + "\n")


def encode(message, key):
    acc = ""
    for i in message:
        new_chr = key + ord(i)
        new_chr = chr(new_chr)
        acc = acc + new_chr
    return acc


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        new_line = encode(line, key)
        outfile.write(new_line + "\n")


def encode_better(s, k):
    acc = ""
    for i in range(len(s)):
        c = s[i]
        key = k[i]
        key = ord(key) - 97
        new_chr = key + ord(c)
        new_chr = chr(new_chr)
        acc = acc + new_chr
    return acc


def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend, "w")
    for line in infile:
        new_line = encode_better(line, pad)
        outfile.write(new_line + "\n")


def main():
    # add other function calls here
    number_words("time.txt", "timeoutput.txt")
    hourly_wages("hourly_wages.txt", "hourly_wages_output.txt")
    calc_check_sum(1234567999)
    send_message("friend.txt", "john")
    send_safe_message("friend.txt", "john", 3)
    send_uncrackable_message("friend.txt", "john", "my_pad.txt")
    pass


main()
