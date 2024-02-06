import random

a = random.random()
a = random.uniform(1, 5)
a = random.randint(1, 10)
a = random.randrange(-3, 10, 2)
a = random.gauss(0, 3.5)

lst = [4, 5, 0, -1, 10, 76, 3]

#a = random.choice(lst)
random.shuffle(lst)
random.seed(123)
a = [random.randint(0, 10) for i in range(20)]
print(a)
