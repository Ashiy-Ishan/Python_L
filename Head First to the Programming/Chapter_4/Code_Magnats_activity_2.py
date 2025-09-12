highest_score = 0
person = ""
result_file = open("result_2.txt")
# access each line
for line in result_file:
    space_index = line.find(" ")
    current_score = line[space_index+1:]
    name = line[:space_index-1]
    if float(current_score) >= highest_score:
        highest_score = float(current_score)
        person = name
    else:
        continue

print(f"{person} {highest_score}")
result_file.close()
