import random

# wylosuj liczbę z zakresu 1 - 100
number = random.randint(1, 100)

while True:
    # pobierz liczbę od użytkownika
    guess = input("Guess the number: ")

    try:
        # spróbuj przekonwertować wprowadzony napis na liczbę całkowitą
        guess = int(guess)
    except ValueError:
        # jeśli nie udało się skonwertować, wyświetl komunikat i kontynuuj pętlę
        print("It's not a number!")
        continue

    # porównaj liczbę wprowadzoną przez użytkownika z wylosowaną liczbą
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("You win!")
        break  # zakończ działanie pętli
