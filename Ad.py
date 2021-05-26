import datetime


class Ad:
    def __init__(self, heading, description, author, date_and_time, number_of_views):
        self.heading = heading
        self.description = description
        self.author = author
        self.date_and_time = date_and_time
        self.number_of_views = number_of_views

    def __str__(self):
        return f"{self.heading}, {self.description}, {self.author}, {self.date_and_time}, {self.number_of_views}"

    def head(self, value):
        if type(value) == str:
            self.heading = value
        else:
            raise TypeError("Ошибка ввода текста")

    def content(self, value):
        if type(value) == str:
            self.description = value
        else:
            raise TypeError("Ошибка ввода текста")

    def view(self):
        self.number_of_views += 1
        return self


date_in_time = datetime.datetime.now()
ad1 = Ad('катушка', 'продам катушку недорого', 'Сергей', str(date_in_time), 0)
ad1.head('Sherman Pro 4000')
ad1.content('Продам катушку! Цена 100 рублей.')
print(ad1.view())
print(ad1.view())