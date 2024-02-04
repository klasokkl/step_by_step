
def get_list():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)

a = get_list()
for x in a:
    print(x)

