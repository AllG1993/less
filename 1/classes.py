class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f'Name: {self.name}\nAge: {self.__age}')


class Employee(Person):

    company = 'Gran'

    def more_info(self):
        print(f'{self.name}\nWorks in: {self.company}')

