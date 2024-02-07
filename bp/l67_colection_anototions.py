from typing import Callable
#mypy
#lst: list = [1, 2, '3', True]
lst: list[int] = [1, 2]
addr: tuple[int, str] = (1, 'string')

elems: tuple[float, ...]
elems = (1.0, 2.0)

words: dict[str, int] = {'one': 1, 'two': 2}

persons: set[str] = {'string', 'shld'}

def get_positive(digits: list[int | float]) -> list[int | float]:
    return list(filter(lambda x: x > 0, digits))

def get_digits(flt: Callable[[int], bool], lst: list[int] = None) -> list[int]:
    if lst is None:
        return []
    return list(filter(flt, lst))

def even(x):
    return bool(x % 2 == 0)

print(get_digits(even, [1, 2, 3, 4])) 
print(get_positive([1, 3, 4]))

