# DECLARATIONS

# gallows_display function checks how many incorrect guesses have been made and draws right number of body parts
# also reports game situation summary to user

def display_gallows(word, hidden_word, incorrect_list):

    body_parts = ["O", "|", "__", "|", "__", "|", "/", "\\"]
    displayed_body_parts = [" ", " ", "  ", " ", "  ", " ", " ", " "]

    for x in range(len(displayed_body_parts)):
        if x < len(incorrect_list):
            displayed_body_parts[x] = body_parts [x]

    gallows = """
        _________________
       |/                |
       |                 {}
       |                 {}
       |               {}{}{}
       |                 {}
       |                {} {}
       |
    ___|___
    """.format(displayed_body_parts[0], displayed_body_parts[1], displayed_body_parts[2], displayed_body_parts[3], displayed_body_parts[4], displayed_body_parts[5], displayed_body_parts[6],
                   displayed_body_parts[7])
    print(gallows)
    print("Lives Left:        " + str(8 - len(incorrect_list)))
    print("Hidden Word:       " + "".join(hidden_word))
    print("Incorrect Guesses: " + ",".join(incorrect_list) + "\n")

# Guess function asks user for a letter and checks that the input is a single letter that hasn't already been attempted
# if the letter is in the target word, the display of hidden word is updated to have stars removed
# list of incorrect guesses is updated

def guess (word, hidden_word, incorrect_list):

    user_letter = input("Choose a letter: ")
    while (user_letter in incorrect_list) or (user_letter in hidden_word) or (not user_letter.isalpha()) or len(user_letter) > 1:
        user_letter = input("Your guess must be a single letter that you haven't already tried. Have another go:  ")
    occurences = 0

    for x in range(len(word)):
        if word[x] == user_letter:
            occurences += 1
            hidden_word[x] = user_letter

    if occurences == 0:
        incorrect_list.append(user_letter)

    return word, hidden_word, incorrect_list

# Game function
# generates random word from list to use as target word
# assigns hidden_word to be string of stars as long as the target word
# assigns incorrect_list to be a list of user guesses that are not in the word
# # calculates number of incorrect guesses when needed by len(incorrect_list)
# runs display_gallows and guess functions in a while loop until loss or victory conditions met

def game ():
    print("Let's play HANGMAN!")
    import random
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'rush', 'south']
    word = random.choice(wordslist)
    hidden_word = list("*" * len(word))

    incorrect_list = []
    win = False

    while (len(incorrect_list)) < 8 and word != "".join(hidden_word):
        display_gallows(word, hidden_word, incorrect_list)
        word, hidden_word, incorrect_list = guess(word, hidden_word, incorrect_list)

    if len(incorrect_list) == 8:
        display_gallows(word, hidden_word, incorrect_list)
        print("Too bad. You got hanged buddy. The word you were looking for was: " + word)
    if word == "".join(hidden_word):
        print("Conratulations! You succesfully guessed that the hidden word was: " + word)

# EXECUTIONS

game()


