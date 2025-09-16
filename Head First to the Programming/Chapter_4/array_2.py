#variables and score
#this code has bug should fix
highest_score = 0
score_list = []
names = []
tempArray = []
person = ''
#open tha file
result_file = open('result_3.txt')

#read all data line by line
for line in result_file:
    (name,score) = line.split()
    score_list.append(float(score))
    tempArray.append(float(score))
    names.append(name)
    if float(score) > highest_score:
        highest_score = float(score)
        person = name

#inhere if i want to create exam same copy of list instead using tempArray = score_list , i can use tempArray = score_list.copy()
def print_name(x):
    for m in range(0,len(tempArray)):
        if x == tempArray[m]:
            return names[m]
    return None

print(names)
print(score_list)
print(tempArray)
score_list.sort()
a = score_list[-1]
print(f'{print_name(a)} {score_list[-1]} \n{print_name(score_list[-2])} {score_list[-2]} \n{print_name(score_list[-3])} {score_list[-3]}')

result_file.close()