highest_score = 0
person = ""
result_file = open("result_2.txt")
# access each line
for line in result_file:
    line_values = line.split()
    current_score = line_values[1]
    name = line_values[0]
    if float(current_score) >= highest_score:
        highest_score = float(current_score)
        person = name
    else:
        continue

print(f"{person} {highest_score}")
result_file.close()