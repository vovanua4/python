import func as vov
spisok = []
spisok.append(vov.load())

# for user in spisok:
#
#     print (user, type(user) ,   "\n")



user = vov.inputUser()

spisok.append(user)

vov.save(spisok)

# print (spisok)