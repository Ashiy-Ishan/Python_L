score = {}

#insert data into list
score[1] = 'Ishan'
score[3] = 'Ashiy'
score[6] = 'Kawish'

#print all value
def option_1():
    for key in score.keys():
        print(score[key] + ' had a score of ' + str(key))

def option_2():
    for key,value in score.items():
        print(value + ' had a score of ' + str(key))

#get option
option = int(input("Enter option 1 or 2 : "))
if option == 1:
    option_1()
else:
    option_2()
