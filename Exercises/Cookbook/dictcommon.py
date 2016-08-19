a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# find keys in common
print (a.keys() & b.keys())

# find keys in a that are not in b
print (a.keys() - b.keys())

# find (key, value pairs in common
print (a.items() & b.items())
