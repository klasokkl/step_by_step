def recursive(value):
    print(value)
    if value <4:
        recursive(value+1)
    print(value)

recursive(1)

def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n-1)

p = fact(6)
print(p)
