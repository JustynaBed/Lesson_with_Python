# TODO 1: Write a program that asks the user to guess a secret number

secretNumber = 5
yourNumber = 0

while yourNumber != secretNumber:
    yourNumber = int(input("Podaj liczbę: "))

    if (yourNumber > secretNumber):
        print("Twoja liczba jest większa od liczby szukanej")
    elif (yourNumber < secretNumber):
        print("Twoja liczba jest mniejsza od liczby szukanej")
    else:
        print("Wygrałeś!")

