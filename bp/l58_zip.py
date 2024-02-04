a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = 'python'


z = zip(a, b, c)
print(list(z))

z = zip(a, b, c)
lz = list(z)
print(*lz)
print(list(zip(*lz)))

