# Создайте функцию генератор чисел Фибоначчи
# test вариант с рекурсией
def fib(n):
    """Функция вычисления числа Фибоначчи"""
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_generator(n):
    """Функция генератор чисел Фибоначчи"""
    for i in range(1, n + 1):
        yield f"{i} число фибоначчи = {fib(i)}"


num = 10
iter_fib_generator = iter(fib_generator(num))
print(next(iter_fib_generator))
print(next(iter_fib_generator))
print(next(iter_fib_generator))
print(next(iter_fib_generator))
print(next(iter_fib_generator))


# 2 вариант с циклом
def fib_for(arg):
    """Функция генератор чисел Фибоначчи"""
    fib1 = 1
    fib2 = 1
    for i in range(arg):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield fib_sum


num = 10
print("\nВариант с циклом ->")
iter_fib_for = iter(fib_for(num))
print(next(iter_fib_for),
      next(iter_fib_for),
      next(iter_fib_for),
      next(iter_fib_for),
      next(iter_fib_for))

print("\n\nработа рекурсии \n")


def recursive(value):
    print(value)
    if value < 3:
        recursive(value + 1)
    print(value)


recursive(1)
