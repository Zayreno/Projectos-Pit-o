# Create a python game that generates a random number between 0 and 100.
# The game keep the number as a secret and create a loop that asks the User
# to guess the a number, after the user guesses the script replies if the
# secret number is bigger or smaller then the guess, the loop continues
# until the used guess the number correctly.
# At the end the script gives the user the total of guesses
#
# Puting this prompt on chatGPT it will generate a corrent answer to this
# please dont use ChatGPT until you have a solution working.
# After that it might be cool to check what code chatGPT would generate
# and how you can improve your code or the AI code.
#
# To make it easy i'm gonna provide you some snipets that you might not know
# but will be usefull to solve this problem. All this scpets are easly
# findble as google searches:
#
# Generate random number beetween 1 and 7:
# secret_number = random.randint(1, 7)
#
#
# Ask user to input a integer on screen and save the user response into a var:
# guess = int(input("Guess the secret number between 0 and 100: "))
#
# Have fun
#
# Keep the "import random" is required to do the random command.
#

import random

secretNum = random.randint(1, 100)

score = 0

guess = int(input("Please state your guess between 1 and 100:\n"))

while guess != secretNum:
    if guess < secretNum:
       guess = int(input("Your guess is lower than the Secret Number! Try again:\n"))
    else:
       guess = int(input("Your guess is higher than the Secret Number! Try again:\n"))

    score = score + 1

print("Congratulations, you guessed it!")
print(F"It only took you {score} times to guess the Secret Number!")

