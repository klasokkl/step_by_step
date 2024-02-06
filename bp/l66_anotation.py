from typing import Union, Optional, Any, Final

MAX_VALUE: Final = 1000


cnt: int = 10
Digit = Union[int, float]
Str = Optional[str]

def mul3(x: int | float, y: Union[int, float] = 2) -> Union[int, float]:
    return x * y

def mul2(x: Digit, y: Any = 2) -> float:
    return x * y

def show_x(x: float) -> None:
    print(f"x = {x}")

res = mul2(5)
res2 = mul3(5)
print(res)
print(mul3.__annotations__)
print(res)
print(mul2.__annotations__)
print(show_x.__annotations__)
