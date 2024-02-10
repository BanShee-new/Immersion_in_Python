# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
list_1 = [6, 6, 1, 2, 3, 4, 5, 5, 1, 1, 5, 3, 3, 3]
double = []
i = 0

while i < len(list_1):
    # print("kol", list_1.count(list_1[i])) для теста
    if list_1.count(list_1[i]) > 1:
        for _ in range(1, (list_1.count(list_1[i]))):
            double.append(list_1.pop(list_1.index(list_1[i], i + 1)))
            # развернуто
            # double.append(list_1[i])
            # list_1.pop(list_1.index(list_1[i], i + test))
    i += 1

print(f"Дубликаты:             {double}")
print(f"Результирующий список: {list_1}")
