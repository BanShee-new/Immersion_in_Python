import itertools
import os
import random
from string import ascii_letters
from random import randint, sample, randbytes


# Задание №test
# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.


def give_two_numbers(name_file: str, count: int):
    with open(name_file, "w", encoding="utf=8") as file:
        for i in range(count + 1):
            file.write(f"{str(random.randint(-1000, 1001)) :>5}\t|\t")
            file.write(str(random.random() * random.randrange(-1000, 1000, 10)) + "\n")


give_two_numbers("new_file.txt", 10)

# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
vowel = 'аеиоуэюя'
consonant = "бвгнджзклмнопрстфхцшщ"
count = 5
rand_name = ""
my_list = []
rand_name += random.choice(consonant).upper()
while (count := count - 1) > 0:
    rand_name += random.choice(consonant)
    rand_name += random.choice(vowel)
print(rand_name)

vowel = 'аеиоуэюя'
consonant = 'бвгнджзклмнпрстфхцшщ'
a = random.randint(4, 7)
v = random.randint(1, a - 2)
s = random.sample(vowel, v) + random.sample(consonant, a - v)
random.shuffle(s)
print(''.join(s).title())

with open('task1.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(s).title())


# ames_size = len(list(test for _ in open('names.txt')))
# nums_size = len(list(test for _ in open('example.txt')))
# count = max(nums_size, names_size)
# with open('res.txt', 'w') as res, \
#         open('task1.txt', 'r') as names, \
#         open('new_file.txt', 'r') as example:
#     names_str = itertools.cycle(names.readlines())
#     example_str = itertools.cycle(example.readlines())
#
#     for i in range(count):
#         example_str1, example_str2 = next(example_str).split('|')
#         prod = float(example_str1) * float(example_str2)
#         if prod < 0:
#             res.write(f'{next(names_str).strip().lower()} {abs(prod)}\n')
#         else:
#             res.write(f'{next(names_str).strip().upper()} {round(prod)}\n')

# ✔Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# ✔расширение
# ✔минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔количество файлов, по умолчанию 42
# ✔Имя файла и его размер должны быть в рамках переданного диапазона.


def makefile(extension, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count_2=42):
    names = set()
    while len(names) < count_2:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))

    for name in names:
        with open(f'{name}.{extension}', 'wb') as file:
            temp = randbytes(randint(min_bytes, max_bytes))
            file.write(temp)
            print(len(temp))


# ✔Доработаем предыдущую задачу.
# ✔Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔Расширения и количество файлов функция принимает в качестве параметров.
# ✔Количество переданных расширений может быть любым.
# ✔Количество файлов для каждого расширения различно.
# ✔Внутри используйте вызов функции из прошлой задачи.


def makefiles(**extension_2):
    for extension, count_2 in extension_2.items():
        makefile(extention=extension, count=count_2)


# temp = {'mp3': 3, 'txt': 5, 'torrent': 2}
# makefiles(**temp)


# ✔Дорабатываем функции из предыдущих задач.
# ✔Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
def makefile_path(path, extension_3):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    makefile(extension_3)

# ✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔Каждая группа включает файлы с несколькими расширениями.
# ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

a = os.listdir()[-1]
print(a.split(".")[-1])
