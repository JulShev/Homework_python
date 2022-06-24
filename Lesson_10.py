import re
import math

res = None
# содаем калькулятор и добавляет обработчики ошибок (исключения)
def operation(a, b, op):
    try:
        if op == "+":
            return float(a) + float(b)
        elif op == "-":
            return float(a) - float(b)
        elif op == "*":
            return float(a) * float(b)
        elif op == "/":
            return float(a) / float(b)
        elif op == "^":
            return math.pow(a, b)
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("на ноль делить нельзя!")

# с помощью регулярного выражения получаем список емаилов, соответствующих заданному условию
while True:
    user_input = input('Введите выражение').replace(' ', '').replace(',', '.')
    if res:
        user_input = user_input.replace('res', str(res))
    find = re.findall(r'^(-?\d+\.?\d*)([-\+\/\*])(-?\d+\.?\d*)$', user_input)
    if find:
        a, op, b = find[0]
        res = operation(a, b, op)
        print(res)

