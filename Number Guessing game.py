import random

def display_instruction():
    print("Welcome To The Number Guessing Game!")
    print("You need to guess a number in 1 to 100.")
    print("You have a limite number of accepts to guess correctly\n")


def start_game():
    securet_number =random.randint(1, 100)
    attempet =10

    for attempets in range(1 ,attempet +1):
        guess =int(input(f"attempets {attempet}\{attempets} - Enter your Guess: ")) 

        if guess < securet_number :
            print("Your guess is to low!")
        elif guess > securet_number:
            print("Your guess is to high!")
        else:
            print(f"Congrulation ,You've guess in number {attempet} attempts.")
            break
    else:
        print(f"Sorry ,You've run out of the .The correct number was {securet_number}")


def number_guessing_game():
    display_instruction()
    while True:
        start_game()
        play_again=input("Do you want to play again (Yes\ No): ").lower()
        if play_again !='yes':
            print("Thanks you for playing the Guessing Game ,GoodBy!")
            break
        
number_guessing_game()