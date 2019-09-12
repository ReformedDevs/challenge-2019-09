from timeit import default_timer as timer
from collections import deque
from random import randint


def is_prime(n, t=5):
    '''
    miller-rabin test
    default to five tests
    '''
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    s, d = 0, n-1
    while d % 2 == 0:
        s, d = int(s+1), int(d/2)

    for _ in range(t):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(1, s):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
        return True


def fib(n):
    seq = deque()
    seq.extendleft([0, 1])
    prv = 1
    cur = 1
    nxt = 0
    while cur < n:
        nxt = cur + prv
        prv = cur
        seq.appendleft(cur)
        cur = nxt
    return seq


def solution(limit, mask):
    start = timer()
    n = max([x for x in fib(limit) if pow(x, 2) & 0xf == mask if is_prime(x)])
    end = timer()
    print(f"pard68, Python 3, {n}, {end - start}, the yeetiest")


if __name__ == "__main__":
    limit = 9000000000000000000
    mask_for = 0x9
    solution(limit, mask_for)
