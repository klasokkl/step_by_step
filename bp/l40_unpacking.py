x, *y = (1, 3, 4, 5, 6)
print(x, y)
*x, y = (1, 3, 4, 5, 6)
print(x, y)
*x, y, z = "hello python"
print(x, y, z)
a = [1, 2, 3]
print((*a,))

d = -5, 5
print(range(*d))
print([*range(*d)])
print([*range(*d), *(True, False), *a])

d = {0: 'ноль', 1: 'one', 2: 'два', 3: 'три', 4: 'четире'}
d2 = {5: 'пять', 6: 'шесть'}
print({*d})
print({*d.values()})
print({*d.items()})
print({**d})
print({**d, **d2})

