k = int(input("Введите число K\n"))

if k < 1:
    print('Число не натуральное')
else:
    if k % 10 == 1 and k % 100 != 11:
        print('Мы нашли '+str(k) + ' гриб в лесу')
    elif (k % 10 == 2 and k % 100 != 12) or \
            (k % 10 == 3 and k % 100 != 13) or \
            (k % 10 == 4 and k % 100 != 14):
        print('Мы нашли '+str(k) + ' гриба в лесу')
    else:
        print('Мы нашли '+str(k) + ' грибов в лесу')
