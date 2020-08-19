from random import choice


def secret_word(word_list=None):
    if not word_list:
        word_list = ['python', 'java', 'kotlin', 'javascript']
    return choice(word_list)


def give_hint(word, char_guessed, anterior_hint=None):
    if not anterior_hint:
        anterior_hint = "-" * len(word)
    current_hint = ""
    for index, character in enumerate(word):
        if anterior_hint[index] != "-":
            current_hint += anterior_hint[index]
            continue
        elif character == char_guessed:
            current_hint += char_guessed
        else:
            current_hint += "-"
    return current_hint


def play():
    word_to_guess = secret_word()
    hint = give_hint(word_to_guess, "")

    tries = 8
    guesses = set()

    while tries > 0:
        print()
        print(hint)
        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("You should print a single letter .")
            continue
        elif not ((letter in "abcdefghijklmnopqrstuvwxyz") and letter.islower()):
            print("It is not an ASCII lowercase letter")
            continue
        elif letter in guesses:
            print("You already typed this letter.")
            continue
        elif letter in word_to_guess:
            hint = give_hint(word_to_guess, letter, hint)
            guesses.add(letter)
            if "-" not in hint:
                print()
                print(hint)
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            tries -= 1
            guesses.add(letter)
            print("No such letter in the word")
    else:
        print("You are hanged!")
        print()


if __name__ == "__main__":

    print("H A N G M A N")
    option = ""

    while option != 'exit':
        option = input('Type "play" to play the game, "exit" to quit:')
        if option == 'play':
            play()