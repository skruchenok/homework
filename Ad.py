import datetime


class Ad:
    def __init__(self, heading, description, author):
        self.heading = heading
        self.description = description
        self.author = author
        self.date_and_time = datetime.datetime.today()
        self.number_of_views = 0

    def __str__(self):
        return f"{self.heading}, {self.description}, {self.author}"

    def edit_head(self, value):
        if type(value) == str:
            self.heading = value
        else:
            raise TypeError("Ошибка ввода текста")

    def edit_content(self, value):
        if type(value) == str:
            self.description = value
        else:
            raise TypeError("Ошибка ввода текста")

    def view(self):
        self.number_of_views += 1
        print(self)


date_in_time = datetime.datetime.now()
ad1 = Ad('катушка', 'продам катушку недорого', 'Сергей')
try:
    ad1.edit_head('Sherman Pro 4000')
    ad1.edit_content('Продам катушку! Цена 100 рублей.')
except TypeError as e:
    print(e)
ad1.view()
print(ad1.number_of_views)
ad1.view()
print(ad1.number_of_views)
ad1.view()
print(ad1.number_of_views)
print(ad1.date_and_time)