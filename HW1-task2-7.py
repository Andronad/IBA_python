"""
KOT + KOT = TOK
"""
for K in range(1, 10):
    for O in range(0, 10):
        for T in range(1, 10):
            KOT = int(str(K) + str(O) + str(T))
            TOK = int(str(T) + str(O) + str(K))
            if KOT + KOT == TOK:
                print(str(KOT) + '+' + str(KOT) + '=' + str(TOK))
                break
            if K+O+T == 27:
                print('Решения нет')

