from random import randint

secret_num = randint(1,11)

guess = 0
while guess != secret_num :
    guess = int(input("Enter the guess : "))
    if guess == secret_num:
        print("You won : bye bye")
        guess = secret_num
    else:
        print("Try again bro : you missed it")