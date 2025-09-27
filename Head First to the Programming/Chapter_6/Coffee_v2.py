#import module
from transaction import *
import starbuzz
import promotion
#functions


items = ["DONUT","LATTE","FILTER","MUFFIN"]
price = [1.5,2.0,1.80,1.20]
running = True

print("Do you have starbuzz card ")
discountTypeCheck = input("Y = YES \nN = NO").lower()

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
        new_price = promotion.discount(price[choice - 1])
        if discountTypeCheck == "y":
            new_price = starbuzz.discount(new_price)
        card = input("Enter the credit card number : ")
        save_transaction(new_price,card,items[choice - 1])