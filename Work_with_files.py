"""
fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written) # 6
fh.close
"""

"""
fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)

fh.close()
"""

"""
fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) ==0:
        break
    print(symbol)

fh.close()
"""

"""
fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthirdline')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()
"""

"""
fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthirdline')
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()
"""

"""
fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second) #'e'

fh.close()
"""

"""
fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)

fh.seek(1)
position = fh.tell()
print(position) #1

fh.read(2)
position = fh.tell()
print(position)

fh.close()
"""
"""
with open("test.txt", "w") as fh:
    fh.write("Some data")
"""

"""
with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)
"""

"""
with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')
"""
"""
s = "Hola!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)
"""

import greetings

message = greetings.great("Holahup")
print(message)

