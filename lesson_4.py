# задание 1
def types_numbers(number: float):
    if number > 0:
        print("положительное")
    elif number < 0:
        print("отрицательное")
    elif number == 0:
        print("ноль")
    else:
        print("Введите число!")


# задание 2
def count_of_words(string_: str):
    set1 = set(string_)
    max_value = 0
    for e in set1:
        if string_.count(e) > max_value:
            max_value = string_.count(e)
    for e in set1:
        if e.isalpha():
            print(f" | {e} | {string_.count(e):<{len(str(max_value))}} |")


count_of_words('Доброго дня')


# Задание 3
input_number = input('inset a number: ')
# заменяем , на .
number = input_number.replace(',', '.')
# проверяем на кол-во точек и дефисов
if number.count("." and "-") <= 1:
    if "-" or "" in number[0]:
        # заменяем -, . на пустоту и проверяем число ли перед нами
            a = number.replace('-', '')
            if (a.replace('.', '').isdigit()) is True:
                if float(number) > 0:
                    print('you entered a positive number')
                elif float(number) < 0:
                    print('you entered a negative number')
                else:
                    print('you entered zero')
            else:
                print("you didn't enter a number4")
    else:
        print("you didn't enter a number2")
else:
    print("you didn't enter a number1")




