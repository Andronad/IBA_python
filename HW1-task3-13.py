import random

n = int(input('Введите n\n'))
if n > 0:
    A = [random.randint(0, 99) for i in range(0, n)]
    print(A)
    B = []
    sum_of_prev = 0
    for i in range(0, len(A)):
        if i != 0:
            sum_of_prev += A[i - 1]
        B.append(sum_of_prev)
    print(B)
else:
    print('n не натуральное')
