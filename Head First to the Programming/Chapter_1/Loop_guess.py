
guess = 0
while guess != 5 :
    guess = int(input("Enter the guess : "))
    if guess == 5:
        print("You won : bye bye")
    else:
        print("Try again bro : you missed it")