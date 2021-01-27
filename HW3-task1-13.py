import datetime


class Bus:
    __fioDriver = 'Unknown'
    __busNumber = '0000xx0'
    __routeNumber = 0
    __brand = 'Unknown'
    __yearOfUsingBegin = 0
    __odometerValue = 0

    def __init__(self, f, bn, rn, b, y, ov):
        self.__fioDriver = f
        self.__busNumber = bn
        self.__routeNumber = rn
        self.__brand = b
        self.__yearOfUsingBegin = y
        self.__odometerValue = ov

    def get_fioDriver(self):
        return self.__fioDriver

    def get_busNumber(self):
        return self.__busNumber

    def get_routeNumber(self):
        return self.__routeNumber

    def get_brand(self):
        return self.__brand

    def get_yearOfUsingBegin(self):
        return self.__yearOfUsingBegin

    def get_odometerValue(self):
        return self.__odometerValue

    def set_fioDriver(self, f):
        self.__fioDriver = f

    def set_busNumber(self, bn):
        if bn[0:4].isnumeric() and bn[6].isnumeric():
            self.__busNumber = bn
        else:
            print('Incorrect bus number')

    def set_routeNumber(self, rn):
        if rn > 0:
            self.__routeNumber = rn
        else:
            print('Incorrect route number')

    def set_brand(self, b):
        self.__brand = b

    def set_yearOfUsingBegin(self, y):
        if 1888 <= y <= datetime.datetime.now().year:
            self.__yearOfUsingBegin = y
        else:
            print('Incorrect year')

    def set_odometerValue(self, ov):
        if ov >= 0:
            self.__odometerValue = ov
        else:
            print('Incorrect value for odometer')

    def get_busAge(self):
        return datetime.datetime.now().year - self.__yearOfUsingBegin

    def __str__(self):
        return ('---\nАвтобус модели ' + self.__brand + ' c номерными знаками ' + str(self.__busNumber) + '\n' +
                'Ввелся в эксплуатацию в ' + str(self.__yearOfUsingBegin) + ' на маршрут ' + str(self.__routeNumber) + '\n' +
                'Пробег ' + str(self.__odometerValue) + '\n' +
                'Водитель: ' + self.__fioDriver+'\n---')


def get_busesForRoute(A, route):
    return list(filter(lambda x: x.get_routeNumber() == route, A))

def get_busesWithSettedAgeOrMore(A, age):
    return list(filter(lambda x: x.get_busAge() > age, A))

A = [Bus('Иванов А.А', '1234XX7', 34, 'BMW', 2013, 10000),
     Bus('Петров К.А', '1512HI7', 34, 'BMW', 2019, 100),
     Bus('Сидоров А.И', '9911XX7', 1, 'Audi', 2013, 40000),
     Bus('Смирнов Б.К', '6280XX7', 2, 'Fiat', 2021, 1100),
     Bus('Иванов Р.Н', '5612XX7', 3, 'Ford', 2001, 430000)]

route = 34
A1 = get_busesForRoute(A, route)
print('Автобусы с маршрутом', route)
for i in range(len(A1)):
    print(A1[i])

age = 1
A2 = get_busesWithSettedAgeOrMore(A, age)
print('Автобусы с возрастом более', age)
for i in range(len(A2)):
    print(A2[i])


