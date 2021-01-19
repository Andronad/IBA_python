k = int(input("Введите число K\n"))

if k < 1:
    print('Число не натуральное')
else:
    if k % 10 == 1 and k % 100 != 11:
        print(str(k) + ' гриб')
    elif (k % 10 == 2 and k % 100 != 12) or \
            (k % 10 == 3 and k % 100 != 13) or \
            (k % 10 == 4 and k % 100 != 14):
        print(str(k) + ' гриба')
    else:
        print(str(k) + ' грибов')
