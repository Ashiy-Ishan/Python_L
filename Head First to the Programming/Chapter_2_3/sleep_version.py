from urllib import request
from time import sleep

# Corrected URL pointing to Chapter_2_3
def get_details():
    page = request.urlopen("https://ashiy-ishan.github.io/Ashinshana_Ishan/")
    text = page.read().decode("utf8")
    place = text.find("<title>")
    print(text[place+7:place+17])

print("1 - Emergency name print \n2 - Print time by time ")
option = input("Option :  ")
if option == "1":
    get_details()
else:
    count = 0
    while count < 3:
        sleep(2)
        get_details()
        count+=1