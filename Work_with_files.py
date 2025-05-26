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

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthirdline')
fh.close()

fh = open('test.txt', 'r')