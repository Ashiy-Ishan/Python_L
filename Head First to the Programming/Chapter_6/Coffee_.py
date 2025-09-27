#import module
from transaction import *
#functions
def discount(old_price):
    return 0.9*old_price

items = ["DONUT","LATTE","FILTER","MUFFIN"]
price = [1.5,2.0,1.80,1.20]
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
        new_price = discount(price[choice-1])
        card = input("Enter the credit card number : ")
        save_transaction(new_price,card,items[choice - 1])