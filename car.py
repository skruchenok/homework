class car:
    def __init__(self, brand, model, color, engine, speed, max_speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine
        self.speed = speed
        self.max_speed = max_speed

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


car1 = car('Nissan', 'Primera', 'blue', 'petrol', 0, 210)
car2 = car('Kia', 'Sportage', 'beige', 'petrol', 40, 180)

try:
    car1.sp(220)
    car1.sp(-150)
    car2.sp(200)
    car2.sp(-100)
    print(car1.speed)
    print(car2.speed)
except TypeError as e:
    print(e)

try:
    car1.col('black')
    car2.col('pink')
    print(car1.color)
    print(car2.color)
except TypeError as e:
    print(e)