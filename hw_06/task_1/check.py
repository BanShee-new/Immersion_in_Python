from sys import argv
from datetime import datetime

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


def check_data(date_inp):
    """Функция проверки даты"""
    *_, year = list(date_inp.split("."))
    try:
        print(date_inp)
        datetime.strptime(date_inp, "%d.%m.%Y").date()
        check_year(int(year))
        return True
    except ValueError:
        print("Некорректная дата")
        return False


def check_year(year):
    """Функция проверки високосного года"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Високосный год")
    else:
        print("не високосный год")


if __name__ == '__main__':
    print("Запускать через консоль (передать дату ДД.ММ.ГГ) !!!")
    print(check_data(*(argv[1:])))
