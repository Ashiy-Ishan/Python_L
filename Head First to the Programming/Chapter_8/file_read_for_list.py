#read file
depots_list = []
depots_file = open("./Depots.txt")
for line in depots_file:
    depots_list.append(line.rstrip())

print(depots_list)