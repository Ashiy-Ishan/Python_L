#import module
from transaction import *

items = ["WORKOUT","WEIGHTS","BICKS"]
price = [35.0,10.0,8.0]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option)+ "."+choice)
        option = option + 1
    print(str(option) + ". for Quit ")
    choice = int(input("Chose an option : "))
    if choice == option:
        running = False
    else:
        card = input("Enter the credit card number : ")
        save_transaction(price[choice-1],card,items[choice - 1])