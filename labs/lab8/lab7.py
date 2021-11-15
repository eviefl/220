"""
Name: evie fleischman
Partner: <your partner's name goes here – first and last>
lab7.py
"""

def encode(message, key):
    acc = ""
    for i in message:
        new_chr = key + ord(i)
        new_chr = chr(new_chr)
        acc = acc+new_chr
    return acc


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