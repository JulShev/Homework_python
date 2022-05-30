# задание 1
number = input("Введите число: ")


if number.isdigit() or number.count(".") <= 1 and number.count("-") <= 1 or number[0] == '-' and number[1:].isdigit():
    number = float(number)

    if number > 0:
        print("положительное", )
    elif number < 0:
        print("отрицательное")
    elif number == 0:
        print("ноль")

else:
    print("Введите число!")


# задание 2
string_ = input("Введите строку: ").lower()
set1 = set(string_)
max_value = 0
for e in set1:
    if string_.count(e) > max_value:
        max_value = string_.count(e)
for e in set1:
    if e.isalpha():
        print(f" | {e} | {string_.count(e):<{len(str(max_value))}} |")
