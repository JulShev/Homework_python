# 6.5
import openpyxl

exel_file = openpyxl.load_workbook("files/users.xlsx")

sheet = exel_file["users"]

print(sheet["A1"])

for i, _ in enumerate(sheet, 1):
    print(sheet[f'A[i]'].value)

for line in sheet:


# 6.4
import csv

FILENAME = "users.csv"
users = [
    {"id": "123456", "name": "Tom", "age": 28},
    {"id": "123456", "name": "Alice", "age": 23},
    {"id": "123456", "name": "Bob", "age": 34}
]
# здесь я открываю файл на запись и называю его file
with open(FILENAME, "w", newline="") as file:
     # здесь я создаю переменную которой присваиваю функцию которая записывает в файл
     writer = csv.writer(file)
     # здесь я вызываю у переменной функцию записывания в файл и передаю значения в файл
     writer.writerow(['id', 'name', 'age', 'phone'])
     # в цикле мы проходимся по каждому юзеру, а затем берем из словаря его значения и создаем на их основе новый список (в который добавляем еще и номер телефона) и потом этот список передаем для записи в функцию writerow
     for user in users:
        writer.writerow([*user.values(), 56405645645])

with open(FILENAME, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# 6.3
import json
people = [
    {"id": "123456",
     "name": "Peter",
     "age": 58
     },
    {"id": "123457",
     "name": "Misha",
     "age": 44
     },
    {"id": "123458",
     "name": "Mary",
     "age": 37
     },
    {"id": "123459",
     "name": "Tim",
     "age": 28
     },
    {"id": "123450",
     "name": "Juli",
     "age": 24
     }
]

with open("data_file.json", "w") as write_file:
    json.dump(people, write_file)


with open("data_file.json") as write_file:
    data = json.load(write_file)
print(data)

# 6.2
first = input('Введите первую строку\r\n')
second = input('Введите вторую строку\n')
third = input('Введите третью строку\n')
forth = input('Введите четвертую строку\r\n')

with open('new_file.txt', "w") as file:
    file.write(first+"\n")
    file.write(second+"\n")

with open('new_file.txt', "a") as file:
    file.write(third++"\n")
    file.write(forth)



 # 6.1
b = b'r\xc3\xa9sum\xc3\xa9'
s = b.decode("UTF-8")
print(s)

s = s.encode("Latin 1")
print(s)

s = b.decode("UTF-8")
print(s)

