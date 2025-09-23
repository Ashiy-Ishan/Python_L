#create function for save transaction
def save_transaction(price,card_number,item_name):
    file = open("transaction.txt", "a")
    file.write("%07d%16s%16s\n"%(price*100,card_number,item_name))
    file.close()
