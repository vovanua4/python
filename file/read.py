import json
file  = open('data' , 'r+')
line = file.readline()
# print (line)
# spisok = []
spisok = json. loads(line)


print(spisok)

