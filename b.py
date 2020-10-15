from math import sqrt, ceil


def is_prime(n: int) -> bool:
    limit = 2000000000
    if n <= 1 or n > limit:
        raise ValueError('Out range argument')
    if n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n+1)), 2):
        if n % i == 0:
            return False
    return True


def main(n: int) -> None:
    if is_prime(n):
        print('prime')
    else:
        print('composite')


if __name__ == "__main__":
    main(73311)
