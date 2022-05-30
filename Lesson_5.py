# задание 1
number = input()
type_of_number = filter(lambda x: x % 2 == 0, number)
print(type_of_number), str(" - четное число")
type_of_number = filter(lambda x: x % 2 != 0, number)
print(type_of_number), str(" - нечетное число")

# задание 2
list_of_numbers = [1, 2, 8, 10, 99, 101]
numbers_to_string = list(map(str, list_of_numbers))

print(numbers_to_string)

# задание 3
words = ('yes', 'level', 'fain')
result = tuple(filter(lambda x: (x == ''.join(reversed(x))), words))

print(result)
