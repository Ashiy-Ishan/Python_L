guess = int (input("Enter your guess : "))

if guess == 5:
    print("Guess is correct : YOU WON")
elif guess > 5:
    if guess > 8:
        print("Too high")
    else:
        print("Bit high")
else:
    if guess < 2:
        print("Very Low")
    else:
        print("Bit low")
