def play_again():
    decision = input("Do you want to play again? \nType 'yes' or 'no'")
    if decision.lower() == "yes" or decision.lower() == "y":
        main()
    elif decision.lower() == "no" or decision.lower() == "n":
        print("Thanks for playing")
    else:
        play_again()

def check_repeat(display, letter):
    return letter in display

def print_display(word):
    screen = ""
    for letter in word:
        screen += "_"
    return screen

def handle_guess(letter, word, display):
    list_string = list(display.replace(" ", ""))
    number = 0
    for i in range(len(word)):
        if word[i] == letter:
            list_string[i] = letter
            number += 1
    display = " ".join(list_string)
    print(f"The letter '{letter}' appears {number} time(s)")
    print(display)
    return display

def win_condition(display, word):
    if display == " ".join(word):
        return True
    return False

def main():
    print("Welcome to Hangman! \nHave someone enter a word to guess")
    hardcode = input().lower()
    guesses = len(hardcode) + 5
    print(f"The word is {len(hardcode)} letters long")
    display_screen = print_display(hardcode)
    win = False

    while guesses > 0:
        print(f"You have {guesses} guess(es) left")
        letter = input("Guess a letter:")
        while len(letter) != 1:
            letter = input("Guess a SINGLE letter:")
        while check_repeat(display_screen, letter) is True:
            letter = input(f"You have already guessed '{letter}'! Guess again:")

        display_screen = handle_guess(letter.lower(), hardcode, display_screen)
        if win_condition(display_screen, hardcode) is True:
            print("Congratulations! You win")
            play_again()
            guesses = 1
            win = True
        guesses -= 1

    if win is False:
        print(f"Sorry you lose! The word was {hardcode}")
        play_again()

if __name__ == "__main__":
    main()