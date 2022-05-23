# 6.1
b = b'r\xc3\xa9sum\xc3\xa9'
s = b.decode("UTF-8")
print(s)

s = s.encode("Latin 1")
print(s)

s = b.decode("UTF-8")
print(s)

