#create function that add new purches to list
def save_transaction(price,credit_card, description):
    file = open("transaction.txt", "a")
    file.write("%s%07d%s\n" %(credit_card,price,description))
    file.close()

def discount(old_price):
    return 0.9*old_price

#intiate product list and all proces
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
        new_price = discount(price[choice - 1])
        credit_card = input("Enter the credit card number : ")
        save_transaction(new_price, credit_card,items[choice -1 ])

