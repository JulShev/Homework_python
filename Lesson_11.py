import re
# создаем генератор геометрической прогрессии

class Generator:
    def __init__(self, number: int, q: int, stop: int):
        self.number = number
        self.stop = stop
        self.q = q

    def __next__(self):
        self.number += 1
        if self.number > self.stop:
            raise StopIteration
        else:
             return  \
                 self.q ** (self.number -1)

    def __iter__(self):
        return self

gen = Generator(1, 4, 20)

for i in gen:
    print(i)


# создаем функцию, которая фильтрует емаил регуляркой
string = """username@hostname
usernamehostname
user123!name@hostname.com
тугканрп
.gkgkj@jj.
4564
"""

email = re.findall(r'[0-9a-zA-Z-\._]+@[0-9a-zA-Z-\._]+', string)
print(email)
