from typing import Union, Sequence


async def max(*numbers: Union[int, float] | Sequence[int | float]) -> int | float:
    numbers_len = len(numbers)
    if numbers_len == 1 and isinstance(numbers[0], Sequence):
        numbers = numbers[0]
        numbers_len = len(numbers)
    a = numbers[0]
    for i in range(1, numbers_len):
        b = numbers[i]
        a = await __max(a, b)
    return a


async def __max(a: int | float, b: int | float) -> int | float:
    return (a + b + abs(a - b)) / 2