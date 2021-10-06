"""
Name: evie fleischman
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    whole_name = input('enter first name and last name: ')
    whole_name = whole_name.split(" ")
    print(whole_name[1] + ', ' + whole_name[0])


def company_name():
    website_url = input('enter a website: ')
    website_url = website_url.split(".")
    print(website_url[1])


def initials():
    name_amount = eval(input("enter how many names will be input: "))
    for i in range(name_amount):
        first_name = input('enter student ' + str(i+1) + ' first name: ')
        print(first_name)
        last_name = input('enter student ' + str(i+1) + ' last name: ')
        print(last_name)
        first_name.split(" ")
        print(first_name + "'s initials: " + first_name[0] + last_name[0])


def names():
    ppl_names = input('enter a list of names, separated by commas: ')
    initial = ppl_names.split(', ')
    for x in initial:
        x = x.split(' ')
        print('The initials are ' + x[0][0] + x[1][0])


def thirds():
    sentence_amount = input('enter how many sentences will be input: ')
    for i in sentence_amount:
        sentence = input('enter sentence ' + str(i) + ': ')
        letter = sentence.split(' ')
        for j in sentence:
            j = j.split(" ")
            print(j[0:3])


def word_average():
    acc = 0
    sen = input('enter a sentence: ')
    words = sen.split(" ")
    for i in words:
        acc = acc + len(i)
    num_words = len(words)
    avg = acc / num_words
    print(avg)


def pig_latin():
    user_sentence = input('enter a sentence: ')
    user_sentence = user_sentence.lower()
    word = user_sentence.split(" ")
    for i in word:
        print(i[1:] + i[0] + 'ay')


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

   # add other function calls here


main()
