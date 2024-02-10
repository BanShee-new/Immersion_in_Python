num = 180_150_001
intermediate = None
res = ""
hex_num = hex(num)
while num > 0:
    intermediate = num % 16
    if intermediate < 10:
        res += str(intermediate)
    elif intermediate == 10:
        res += "a"
    elif intermediate == 11:
        res += "b"
    elif intermediate == 12:
        res += "c"
    elif intermediate == 13:
        res += "d"
    elif intermediate == 14:
        res += "e"
    elif intermediate == 15:
        res += "f"
    num //= 16

print("ваш ответ в шестнадцатеричной системе -> ", res[::-1])
print("\tПроверка -> ", hex_num[2:])

# продвинутый вариант
num = int(input("Введите число для перевода в 16-ную систему -> "))
# 180_150_001
res = ""
hex_num = hex(num)
system_16 = '0123456789abcdef'
system = 16

while num > 0:
    res += system_16[num % system]
    num //= system

print("ваш ответ в шестнадцатеричной системе -> ", res[::-1])
print("\tПроверка -> ", hex_num[2:])
