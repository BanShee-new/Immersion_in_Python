import csv
import json
import os
import pickle

# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.

def file_transform(file_name):
    new_dict = dict()
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            num, *_, num_float = line.strip().split()
            num_float = round(float(num_float), 1)
            new_dict[num] = num_float
    with open("text_to_json.json", "w", encoding="utf-8") as file_2:
        json.dump(new_dict, file_2, ensure_ascii=False, indent=3)
    return new_dict


# print(my_dict := file_transform("text.txt"))
# print("\n Проверка -> ")
# with open("text_to_json.json", "r", encoding="utf-8") as file_3:
#     my_dict_2 = json.load(file_3)
# print(my_dict_2)

# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от test до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключом для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


def asking_name():
    flag = 3
    while flag > 0:
        try:
            name, pers_id, level = input('Введите данные: ').split()
        except ValueError:
            print("ошибка ввода, три элемента через пробел пожалуйста)")
            continue
        dict_line = {pers_id: {name: level}}
        with open('my_file.json', 'a', encoding="utf-8") as f:
            json.dump(dict_line, f, indent=3, ensure_ascii=False, sort_keys=True)
        flag -= 1


# asking_name()

def task_4():
    with open("my_file.json", "r", encoding="utf-8") as file_1:
        data = json.load(file_1)
        result = []
        print(type(data))
        for key, value in data.items():
            result.append((key, value))
        print(result)
    with open("my_file.csv", 'w', encoding="utf-8", newline='') as file_2:
        writer_1 = csv.writer(file_2, delimiter=';')
        writer_1.writerows(result)


# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
def to_json():
    for name_file in os.listdir():
        if name_file.endswith(".json"):
            with open(f"{name_file}", "r", encoding="utf-8") as file_read:
                data = json.load(file_read)
            with open(f"{name_file[:-5]}.pickle", "wb") as file_write:
                pickle.dump(data, file_write)


# to_json()


