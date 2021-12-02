"""
Name: evie fleischman
lab11.py
"""

from random import randint


def file_words():
    file = open("wordlist.txt", "r")
    words = file.readlines()
    file.close()
    return words


def pick_word(words):
    move = randint(0, len(words) - 1)
    return words[move]


def guessed_letters(chosen, guess, acc, count):
    guessed = False
    chosen = chosen.lower()
    for i in range(len(chosen)):
        if chosen[i] == guess:
            acc[i] = guess
            guessed = True
    if guessed:
        return "" .join(acc)
    else:
        return count + 1


def finished_game(acc):
    for i in range(len(acc)):
        if acc[i] == "_":
            return False
    return True


def play():
    file_words()
    words = file_words()
    chosen = pick_word(words)
    acc = list()
    for i in range(len(chosen)):
        acc.append("_")
    used_letters = list()
    count = 0
    guessed_words = acc
    while not finished_game(acc):
        if count <= 7:
            guess = input("pick a letter")
            holder = guessed_letters(chosen, guess, acc, count)
            if str(holder).isnumeric():
                if guess in used_letters:
                    count = count
                else:
                    count = holder
            else:
                guessed_words = holder
            print("".join(guessed_words))
            used_letters.append(guess)
            print("wrong tries attempted: " + str(count) + " out of 7")
            print("letters already guessed: ", "," .join(used_letters))
        else:
            print("you lose!")
            return
    else:
        print("winner!")
        return


def main():
    play()
    pass


main()
