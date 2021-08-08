# класс
# атрибут класса
# экземпляр класаа
# атрибут экземплляра класса
# метод экземпляра класса

# class MyFirstClass:
#     some_string = 'TEST'  # атрибут класса
#     value = 0   # атрибут класса
#
#
# MyFirstClass.some_string = 'new test'
# test_value = MyFirstClass.some_string
# new_value = MyFirstClass.value
# print(test_value, new_value)

# class Person:
#     name = 'John'
#     surname = 'Wick'
#     age = 23
#     sex = 'Male'
#
#
# # if Person.age < 50:
# #     print(f'Ты молодой человек, {Person.name} {Person.surname}')
#
# person_1 = Person()  # экземпляр класса
# person_1.address = 'Dnipro'
# print(person_1.address)
# person_2 = Person()  # экземпляр класса
#
# print(person_1.name)
# print(person_2.name)
# print('-------------------')
# person_1.name = 'Vova'
# print(person_1.name)
# print(person_2.name)
# print('-------------------')
# Person.name = 'Jack'
# print(person_1.name)
# print(person_2.name)


class Person:
    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.switch_sex()

    def __str__(self):
        return f'Person: {self.name} {self.surname}, age: {self.age}, sex: {self.sex}'

    def __repr__(self):
        return f'{self.name} {self.surname}, {self.age}, {self.sex}'

    def increase_age(self):
        self.age += 1

    def switch_sex(self):
        sex_dict = {'Male': 'Female', 'Female': 'Male'}
        self.sex = sex_dict[self.sex]


person_1 = Person('John', 'Wick', 23, 'Male')
print(person_1)
person_1.increase_age()
person_1.switch_sex()
print(person_1)
# person_2 = Person('Jane', 'Foster', 21, 'Female')
# list_persons = [person_1, person_2]
# print(person_2)
# print(list_persons)