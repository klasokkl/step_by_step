def is_prost(x):
    d = x - 1
    if d < 0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d -= 1
    return True

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = filter(lambda x: x % 2 == 0, a)

print(list(b))

c = filter(is_prost, a)
print(list(c))

t = filter(is_prost, a)
t2 = filter(lambda x: x % 2 != 0, t)
print(list(t2))
