import random, time
from argparse import ArgumentParser
arg= ArgumentParser()
arg.add_argument( 'a', help= "int do kakogo", type=int , default=10)
do = 10


avgr = 0

objCount = 0
objWin = 0

masivChisel = {0:0,
               1: 0,
               2: 0,
               3: 0,
               4: 0,
               5: 0,
               6: 0,
               7: 0,
               8: 0,
               9: 0,
               10: 0,
               }


def genrator1():
    return int(random.randint(0 ,do))

def genrator2():
     return int(random.randint(0 ,do))


def genrator3():
    return int(random.randint(0, do))
count =0
masivChisel = {}
spinCoun = 0
spinSleep = 1000

while True:
    
    
    gen1 = genrator1()
    gen2 = genrator2()
    gen3 = genrator3()


    if gen1==gen2==gen3:
        objWin +=1
        objCount +=count
        spinCoun += 1

        countChisel = masivChisel.get(gen1, 0)
        countChisel = int(countChisel) + 1
        masivChisel[gen1] = countChisel

        print ('ok '+ str(spinCoun))


        if spinCoun> spinSleep:
            spinCoun = 0
            avgr = objCount / objWin

            print('-'*80 )
            print('-'*80 )
            print('-'*80 )
            # print(dictInt , type(dictInt))
            # dictInt(gen1)+= 1
            # dictInt.gen1 += 1



            # print(countChisel, type(countChisel))

            # print(masivChisel, )




            print ('|%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s|   |||%4s|||' % (0, 1, 2, 3, 4,5,6,7,8,9,10,'avr'))
            print ('|%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s| |%3s|   |||%4s|||' % (masivChisel.get(0 ,0),
                                                                               masivChisel.get(1, 0),
                                                                               masivChisel.get(2, 0),
                                                                               masivChisel.get(3, 0),
                                                                               masivChisel.get(4, 0),
                                                                               masivChisel.get(5, 0),
                                                                               masivChisel.get(6, 0),
                                                                               masivChisel.get(7, 0),
                                                                               masivChisel.get(8, 0),
                                                                               masivChisel.get(9, 0),
                                                                               masivChisel.get(10, 0),
                                                                                                      avgr


                                                                               ))

            print ('|%s| |%s| |%s|  === |%s| ' % (gen1 , gen2 , gen3, count))

            print('-' * 80)
            print('-' * 80)
            print('-' * 80)


            time.sleep(1)
        count = 0



    else:
        count += 1
        # print ('|%s| |%s|  |%s| '  % (gen1 , gen2, gen3))