# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.

hike = {"Вова": ("шампур", "печеньки", "мясо", "вода"),
        "Саша": ("шоколад", "палатка", "вода", "бумага", "удочки"),
        "Маша": ("печеньки", "мяч", "бумага", "салфетки", "вода")}
# вытаскиваем всех друзей (список друзей)
friends = []
for i in hike:
    friends.append(i)

# Какие вещи взяли все три друга
set_all = set()
for j in hike.values():
    set_all |= set(j)
print(f"Весь хабар: {str(set_all).rjust(123)}")
print("Весь хабар(стационарная проверка): ", set(hike["Вова"]) | set(hike["Саша"]) | set(hike["Маша"]))
print("объединение множеств (так-же можно использовать метод '.union')\n")

# Какие вещи уникальны, есть только у одного друга (переменная whom_we_check = кого проверяем ?)
whom_we_check = "Вова"
set_unique = set(hike[whom_we_check]).copy()

for key, value in hike.items():
    if key == whom_we_check:
        continue
    set_unique -= set(value)
print(f"Уникальные вещи у Вовы: {str(set_unique).rjust(42)}")
print("Уникальные вещи у Вовы(стационарная проверка): ", set(hike["Вова"]) - set(hike["Саша"]) - set(hike["Маша"]))
print("Разность множеств (так-же можно использовать метод '.difference()'\n")

# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует (search = что ищем?)
search = "бумага"
for name, things in hike.items():
    if search in things:
        print(f"У {name}\bи есть {search} !")
    else:
        print(f"У {name}\bи нет {search}\bи !")

print("---" * 50)
# Сделал дополнительно: какие вещи есть у всех друзей?
set_intersect = set(hike["Вова"]).copy()
for k in hike.values():
    set_intersect = set_intersect & set(k)

print(f"Эти вещи есть у всех друзей: {str(set_intersect).rjust(32)}")
print("Эти вещи есть у всех друзей(стационарная проверка): ", set(hike["Вова"]) & set(hike["Саша"]) & set(hike["Маша"]))
print("пересечение множеств (так-же можно использовать метод .intersection() для записи пересечений)")

# постарался сделать код максимально гибким (input-ами не стал заморачиваться (но передать в переменные/функции можно))
# и можно добавить друзей
print("---" * 50)
hike["Ваня"] = ("бумага", "мяч", "столик", "вода")
search = "бумага"
for name, things in hike.items():
    if search in things:
        print(f"У {name}\bи есть {search} !")
    else:
        print(f"У {name}\bи нет {search}\bи !")
