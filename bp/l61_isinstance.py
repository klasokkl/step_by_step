
data = (4.5, 8.7, True, "книга", 8, 10, -11, [True, False])

s = 0
for x in data:
    if isinstance(x, float):
        s += x
print(s)

s = sum(filter(lambda x: isinstance(x, float), data))
print(s)
s = sum(filter(lambda x: type(x) is int, data))
print(s)


