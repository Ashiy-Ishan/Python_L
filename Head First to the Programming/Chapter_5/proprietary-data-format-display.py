
user_details = {}

#real text tile
file = open("proprietary_data_1.txt")
for line in file:
    (u_id,u_name,u_country,u_avg,u_board,u_age) = line.split(';')
    user_details['id'],user_details['name'],user_details['country'],user_details['avg'],user_details['boart_type'],user_details['age'] = u_id,u_name,u_country,u_avg,u_board,u_age

    print(f"Id:           {user_details['id']}")
    print(f"Name:          {user_details['name']}")
    print(f"Country:       {user_details['country']}")
    print(f"Average:       {user_details['avg']}")
    print(f"Boart type:    {user_details['boart_type']}")
    print(f"Age :          {user_details['age']}")
    print("----------------------------------------------------")


file.close()