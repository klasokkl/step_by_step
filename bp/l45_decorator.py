import time
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("перед визовом функции")
        res = func(*args, **kwargs)
        print("после визова функции")
        return res
    return wrapper


def some_func(title, tag):
    print(f"визов функции some_func {title} {tag}")
    return f"{title} {tag}"

some_func = func_decorator(some_func)
res = some_func('python', 'h1')
print(res)


def test_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        dt = stop - start
        print(f"время работи функции {dt}")
        return res
    return wrapper

@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

#get_nod = test_time(get_nod)
res = get_nod(2, 10000)
print(res)

#get_fast_nod = test_time(get_fast_nod)
res2 = get_fast_nod(2, 10000)
print(res2)
