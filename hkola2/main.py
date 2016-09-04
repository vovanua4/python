import pickle


# print (dir(pickle))
# fail = open ( 'xxx.bin' , 'wb' )



# a = 1
# pick = pickle.dumps(a , 4);  ##кодирование в сттроку
# pick = pickle.dump(a ,fail );  ##кодирование в фаил




# orig = pickle.loads(pick) ## декодир
# origFail = pickle.load(fail) ## декодир


# print(origFail )


# import shelve
# db = shelve.open('www')


# db['1'] = [1,2,3,4]
# db['2'] = 'stroka'
# db.close()


# db2 = shelve.open('www')
# print(db2.keys())


# import  json
#
#
# a = ['stroka', 'stroka2']
#
# strJson  = json.dumps(a, separators=('\n',' '), indent= 4)
#
# print (strJson , type(strJson))

# orig = json.loads(strJson)




# print( pick)



import os
print(os.name)

os.mkdir('sss/wwww')


