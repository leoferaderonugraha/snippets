from typing import Dict


ComputeCache: Dict[int, int] = {}


def fib(n: int) -> int:
    if n in ComputeCache:
        return ComputeCache[n]

    if n == 0 or n == 1:
        ComputeCache[n] = n
    else:
        ComputeCache[n] = fib(n - 1) + fib(n - 2)

    return ComputeCache[n]


if __name__ == '__main__':
    print(f"fib(55): {fib(55)}")
