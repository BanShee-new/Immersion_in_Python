class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя животного: {self.name}, Возраст: {self.age}'

    def action(self):
        return f'у {self.name} действие не определенно'


class Fish(Animal):
    def __init__(self, breed, name, age):
        super().__init__(name, age)
        self.breed = breed

    def action(self):
        print('Я плаваю !')

    def __str__(self):
        return super().__str__() + f', Вид: {self.breed}'


class Dog(Animal):
    def __init__(self, breed, name, age):
        super().__init__(name, age)
        self.breed = breed

    def action(self):
        print('Я гавкаю !')

    def __str__(self):
        return super().__str__() + f', Порода: {self.breed}'


class Bird(Animal):
    def __init__(self, breed, name, age):
        super().__init__(name, age)
        self.breed = breed

    def action(self):
        print('Я пою !')

    def __str__(self):
        return super().__str__() + f', Вид: {self.breed}'


class AnimalFactory:
    def __new__(cls, type_class, *args):
        instance = type_class(*args)
        return instance


fish = AnimalFactory(Fish, 'Форель', 'Мисси', 1)
fish_2 = AnimalFactory(Fish, 'Селедка', 'Вкусная', 1)
bird = AnimalFactory(Bird, 'Попугай', 'Лютик', 3)
dog = AnimalFactory(Dog, 'Спаниель', 'Лайка', 5)
dog_2 = AnimalFactory(Dog, 'Хот-дог', 'Сосиска', 0)
list_animals = [fish, fish_2, bird, dog, dog_2]

for animal in list_animals:
    print(animal)
    animal.action()


# fish = Fish('Форель', 'Мисси', 3)
# dog = Dog('Спаниель', 'Лайка', 5)
# bird = Bird('Попугай', 'Лютик', 3)
# animal_list = [fish, dog, bird]
# for animal in animal_list:
#     print(animal, end=f"{'->' :>5} ")
#     animal.action()


# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


# class AnimalFactory:
#     @staticmethod
#     def add_animal(class_, breed, name, age):
#         if class_ == Fish:
#             return Fish(breed, name, age)
#         elif class_ == Dog:
#             return Dog(breed, name, age)
#         elif class_ == Bird:
#             return Bird(breed, name, age)
#
#
# fish_1 = AnimalFactory.add_animal(Fish, 'Форель', 'Мисси', 3)
# dod_1 = AnimalFactory.add_animal(Dog, 'Спаниель', 'Лайка', 5)
# bird_1 = AnimalFactory.add_animal(Bird, 'Попугай', 'Лютик', 3)
# list_animal = [fish_1, dod_1, bird_1]
# for animal in list_animal:
#     print(animal, end=f"{'->' :>5} ")
#     animal.action()
