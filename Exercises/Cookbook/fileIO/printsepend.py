# -*- coding: utf-8 -*-


print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!\n')


for i in range(5):
    print(i)

for i in range(5):
    print(i, ' ')


row = ('ACME', 50, 91.5)
print(*row, sep=',')
print(row, sep=',')
