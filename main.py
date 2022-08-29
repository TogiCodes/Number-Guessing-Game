import os
import random

os.system("cls") #clears the console

game_running = True

def guess():
    returning = input("Select a number between 1, 100: ")
    if not returning.isdigit():
        print("Invalid Input")
        return guess()
    elif int(returning) < 1 or int(returning) > 100:
        print("Invalid Input")
        return guess()
    else:
        return int(returning);

num_to_guess = random.randint(1, 100)
print(num_to_guess) #for the video
while game_running:
    user_guess = guess()
    if user_guess == num_to_guess:
        print(f"You got it right: {num_to_guess}")
        game_running = False
    else:
        print("Wrong number, try again")

#? Don't forget to like, subscribe and comment
