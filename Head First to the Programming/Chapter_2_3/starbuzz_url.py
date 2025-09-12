from urllib import request

# Corrected URL pointing to Chapter_2_3
#used my weblink for get site details otherwise provided link not works
page = request.urlopen("https://ashiy-ishan.github.io/Ashinshana_Ishan/")
text = page.read().decode("utf8")
place = text.find("<title>")
print(text[place+7:place+17])