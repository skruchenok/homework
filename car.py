class Car:
    def __init__(self, brand, model, color, engine, speed, max_speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine
        self.speed = speed
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.speed}, {self.max_speed}, {self.brand}, {self.model}"

    def sp(self, value):
        # print(type(value)) # можно раскомментить и посмотреть реальный тип параметра
        if type(value) == int:
            self.speed += value
            if self.speed > self.max_speed:
                self.speed = self.max_speed
            if self.speed < 0:
                self.speed = 0
        else:
            raise TypeError("Ошибка ввода числа")

    def col(self, new_color):
        if type(new_color) == str:
            self.color = new_color
        else:
            raise TypeError("Ошибка ввода цвета")


def lst(n=int(input('Введите количество авто:'))):
    lst_speed = []
    while n != 0:
        lst_speed.append('car' + str(n) + '.max_speed')
        n -= 1
    return lst_speed


def searh(lst_car, max_speed):
    for brand in lst_car:
        if isinstance(brand, Car):
            if max_speed == max_speed:
                return brand


car1 = Car('Nissan', 'Primera', 'blue', 'petrol', 0, 210)
car2 = Car('Kia', 'Sportage', 'beige', 'petrol', 40, 180)

# try:
#     car1.sp(220)
#     car1.sp(-150)
#     car2.sp(200)
#     car2.sp(-100)
#     print(car1.speed)
#     print(car2.speed)
# except TypeError as e:
#     print(e)
#
# try:
#     car1.col('black')
#     car2.col('pink')
#     print(car1.color)
#     print(car2.color)
# except TypeError as e:
#     print(e)
# lst_speed=[car1.max_speed, car2.max_speed]
# print(lst_speed)
# M = max(lst_speed)
# print(M)
# lst = [car1, car2]
# print(searh(lst, M))
# print(lst())
# lst_speed = lst()
# M = (max(lst_speed))
# print(M)