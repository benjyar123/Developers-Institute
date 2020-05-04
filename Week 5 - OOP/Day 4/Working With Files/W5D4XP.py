# Exercise 1
# (Code along with Yair)

import random

def get_words_from_file():
    with open("words.txt", "r") as f:
        words = [word.replace("\n", "") for word in f.readlines()]
        return words

def get_random_sentence(length):
    words = get_words_from_file()
    sentence = random.choices(words, k=length)
    return ", ".join([word for word in sentence])

def main():
    print("....This is an explanation...")
    length = ask_user()
    print(get_random_sentence(length))

def ask_user():
    while True:
        l = input("length of sentence between 2 and 20")
        if not l.isdigit():
            print("Input needs to be a digit")
            continue
        elif int(l) > 20 or int(l) < 2:
            print("Input needs to be between 2 and 20")
            continue
        else:
            break
    return int(l)





if __name__ == '__main__':
    main()
