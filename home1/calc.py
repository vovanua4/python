#@auvtor Matysh Vladimir
name =  input('>>> ваше имя ')
c = 'привет друг ' + name

print(''.center(80, '-'))
print(c.center(80, '='))
print("калькулятор".title().center(80, '='))

print(''.center(80, '-'))

print ("1 +")
print ("2 -")
print ("3 /")
print ("4 x")
actions = str(input('выберите действие ' + name + '!!!!!'))
if actions.isdigit():
    print("#" * 80)
    print('\n' * 2)
    first = str(input('первое число  '))
    if first.isdigit():
        second = str(input('второе число  '))
        print('\n' * 2)
        if second.isdigit() :
            if actions == "1":
                intRezylt = int(first) + int(second)
                print ('сумма чисел' + first + ' и ' + second  + " равно " + str(intRezylt))
            elif actions == '4':
                intRezylt = int(first) * int(second)
                print ('если умножить ' + first + ' на ' + second  + " то получится  " + str(intRezylt))
            elif actions == '3':
                intRezylt = int(first) / int(second)
                print ('если разделить ' + first + ' на ' + second  + " то получится " + str(intRezylt))
            elif actions == '2':
                intRezylt = int(first) - int(second)
                print ('если отнять ' + first + ' от ' + second  + "то получится " + str(intRezylt))
            else:
                print("-=неправельно действие =-".capitalize().center(80 , "-"))

            print('\n' * 2)

            print("+-" * 40)
            print("+-" * 40)
            print("конец".upper().center(80, "-"))

            print("+-" * 40)
        else:
            print ('-= не число =- '.upper().center(80 ,"-"))
else:
    print('-= не число =- '.upper().center(80 ,"-"))