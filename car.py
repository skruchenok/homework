class car:
    def __init__(self, brand, model, color, engine, speed, max_speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine
        self.speed = speed
        self.max_speed = max_speed

    def sp(self, value):
        self.speed += value
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0


car1 = car('Nissan', 'Primera', 'blue', 'petrol', 0, 210)
car2 = car('Kia', 'Sportage', 'beige', 'petrol', 40, 180)
# car1.sp(40)
# print(car1.speed)
# car1.sp(40)
# print(car1.speed)
# car1.sp(-100)
# print(car1.speed)