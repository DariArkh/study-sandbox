from random import *

print("Welcome to the number guessing game!")

def is_valid(s, max_value):
    if s.isdigit() and 1 <= int(s) <= max_value:
        return True
    else:
        return False

def guess_game():
    print("Please enter the maximum number to guess")
    max_num = input()
    max_num = int(max_num)
    n = randint(1, max_num)
    print(f"Enter an integer from 1 to {max_num}")
    counter = 0    
    while True:
        guess = input()
        if is_valid(guess, max_num):
            num = int(guess)
            if num < n:
                print("Your number is less than the guessed one, try again")
                counter += 1
            elif num > n:
                print("Your number is higher than the guessed one, try again")
                counter += 1
            else:
                print("You guessed it, congratulations!")
                print(f"You guessed the number on your {counter} try.")
                counter += 1
                break

        else:
            print(f"You should enter an integer from 1 to {max_num}")

def game_continue():
    while True:
        print("Would you like to continue? yes/no")
        answer = input().lower()    
        if answer == "yes":
            guess_game()
        elif answer == "no":
            print("Thanks for playing the number guessing game. See you later...")
            break
        else:
            print("yes or no?")            

guess_game()
game_continue()    
    