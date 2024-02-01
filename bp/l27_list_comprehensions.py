
N = 6 
#a = [0] * N
#for i in range(N):
#    a[i] = i ** 2
a = [x ** 2 for x in range(N)]

print(a)

a = [ord(d) for d in "python"]
print(a)

a = [x for x in range(-5, 5) if x < 0]
print(a)

