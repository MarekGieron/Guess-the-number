import random

# pick a number 1 - 100
number = random.randint(1, 100)

while True:
    # get number from user
    guess = input("Guess the number: ")

    try:
        # try to convert the entered string to integer
        guess = int(guess)
    except ValueError:
        # if the conversion failed, display a message and continue the loop
        print("It's not a number!")
        continue

    # compare the number entered by the user with the number drawn
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("You win!")
        break  # end the loop
