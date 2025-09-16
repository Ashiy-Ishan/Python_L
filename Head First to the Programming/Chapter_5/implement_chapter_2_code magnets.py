#create variable and hash
scores_name = {}

#open file
result_file = open("../Chapter_4/result_3.txt")
#real file
for line in result_file:
    (name,score) = line.split()
    scores_name[float(score)] = name

#sort dictionary
print(scores_name)
#print options
def without_sorting():
    for key,value in scores_name.items():
        print(f'{value} {key}')

def with_sorting():
    for key in sorted(scores_name.keys(),reverse=True):
        print(f'{key}')

def with_sorting_name():
    for key in sorted(scores_name.keys(),reverse = True):
        print(f'{scores_name[key]} {key}')

#option run
option = int(input("Type number of option :"))
if option == 1:
    without_sorting()
elif option == 2:
    with_sorting()
else:
    with_sorting_name()