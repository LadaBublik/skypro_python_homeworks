class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.lastname = last_name

    def myName(self):
        print('Меня зовут', self.name)

    def myLastName(self):
        print('Моя фамилия', self.lastname)

    def myNameAndLastName(self):
        print('Меня зовут', self.name, 'моя фамилия', self.lastname)
