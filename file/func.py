import json

def load(nameFail="data.txt"):
    fail  = open(nameFail, "r")
    failStr = fail.readline()
    spisok = json.loads(failStr)
    # user = spisok[0][0]
    # print(user , type(user))
    return spisok



def save ( spisok  , nameFaile="data.txt" ):
    file = open(nameFaile, 'w')
    json_spisok = json.dumps(spisok)
    file.write(json_spisok)
    file.close()

def inputUser():
    print("записать пользователя")
    user = {}
    user.update({'first': input("Фамилия")})
    user.update({'name': input("Имя")})
    user.update({'date': input("дата рождения")})
    user.update({'email': input("email")})
    user.update({'site': input("site")})
    user.update({'tel': input("тел")})
    return user


