record = '....................100 .......513.25 ..........'

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print cost

# obj a              a.start  a.stop  a.step
a = slice(5, 50, 2) #  5        50      2

s = 'HelloWorld'
# indices cut the range to a optimium range
for i in range(*a.indices(len(s))):
    print s[i]
