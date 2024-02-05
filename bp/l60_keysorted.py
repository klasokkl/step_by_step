def is_odd(x):
    return x % 2

def key_sort(x):
    return x if x % 2 == 0 else 100 + x


a = [4, 3, -10, 1, 7, 12]
#b = sorted(a, key=is_odd)
#b = sorted(a, key=lambda x: x % 2)
a.sort(key=lambda x: x % 2)
b = sorted(a, key=key_sort)


print(a)
print(b)
