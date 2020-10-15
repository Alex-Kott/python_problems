from functools import lru_cache
from math import sqrt, ceil
from typing import List


@lru_cache()
def is_prime(n: int) -> bool:
    if n < 1:
        raise ValueError('Out range argument')
    if n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


@lru_cache
def is_hyperprime(n: int) -> bool:
    for i in split_number(n):
        if not is_prime(i):
            return False
    return True


def split_number(n: int) -> List[int]:
    number_list = []
    number_str = ""
    for s in str(n):
        number_str += s
        number_list.append(int(number_str))

    return number_list


def main() -> None:
    a, b = input('Input range boundaries: ').split(' ')
    hyperprimes = set()
    for n in range(int(a), int(b)+1):
        if is_hyperprime(n):
            hyperprimes.add(n)

    if not hyperprimes:
        print(0)

    for i in hyperprimes:
        print(i, end=" ")


if __name__ == "__main__":
    main()
