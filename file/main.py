import  json

print("записать пользователя")
user = {}
user.update( {'first': input("Фамилия") })
user.update({'name': input("Имя") })
user.update({'date': input("дата рождения") })
user.update({'email': input("email") })
user.update({'site': input("site") })
user.update({'tel': input("тел") })

print('\n' *2)
spisok = []
# print( user)
fail = open("data", 'r+')
jsonSpisok = fail.read()
# print(jsonSpisok)
spisok = json.loads(jsonSpisok)
spisok.append(user)
userJson = json.dumps(spisok , sort_keys=True)

fail.write(userJson + "\n")
fail.close()
