#declair hash
all_data = {}
temp = {}
def line_process(x):
    file = open("proprietary_data_1.txt")
    for line in file:
        (u_id, u_name, u_country, u_avg, u_board, u_age) = line.split(';')
        all_data['id'], all_data['name'], all_data['country'], all_data['avg'], all_data[
            'boart_type'], all_data['age'] = u_id, u_name, u_country, u_avg, u_board, u_age
        if x == int(all_data['id']):
            return all_data
        else:
            continue
    file.close()
    return 0
input_id = int(input('Enter user id  :'))
#call function
temp = line_process(input_id)
print(temp)


