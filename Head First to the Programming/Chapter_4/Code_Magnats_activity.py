highest_score = 0
result_f = open("result_1.txt")

for line in result_f:
    if int(line) > highest_score:
        highest_score = int(line)

print(highest_score)
result_f.close()