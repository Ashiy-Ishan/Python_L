import sqlite3
#declair hash
all_data = {}
temp = {}
def row_process(x):
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row['id']==x:
            all_data['id'],all_data['name'],all_data['board'] = row['id'],row['name'],row['board']
            return all_data
        else:
            continue
    cursor.close()
    return 0
input_id = int(input('Enter user id  :'))
#call function
temp = row_process(input_id)
if temp:
    print("ID is " + str(temp['id']))
    print("Name is " + temp['name'])
    print("Board-type is " + temp['board'])


