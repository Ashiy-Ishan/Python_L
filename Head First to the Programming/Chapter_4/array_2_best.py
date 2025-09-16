
results = []
#loop for read things
score_list = open("result_3.txt")

#loop
for line in score_list:
    (name,score) = line.split()
    score = float(score)
    results.append((score,name))

#sort array
results.sort()
#get only top 3 results
top_3 = results[-3:]

for (score,name) in reversed(top_3):
    print(f'{name} : {score}')

score_list.close()