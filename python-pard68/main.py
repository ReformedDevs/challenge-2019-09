from timeit import default_timer as timer
from collections import deque
from random import randint


def is_prime(n):

    """
    Primality Test
    A basic naive test followed by the Miller-Rabin
    """

    # Run a basic naive prime test
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Now run the Miller-Rabin Test
    return miller_rabin(n)


def decompose(n):

    """
    Decompose `n` into `d` and `s`
    Returns `d` and `s`
    """

    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = int(s + 1), int(d / 2)
    return (s, d)


def miller_rabin(n, t=5):

    """
    The Miller-Rabin Primality Test
    Takes:
    n: the number being tested
    t: the number of tests to run, defaults to 5
    Returns False if `n` is composite
    Returns True if `n` probably is prime
    """

    s, d = decompose(n)
    for _ in range(t):
        x = pow(randint(2, n - 1), d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(1, s):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def fib(n):

    """
    Finds the Fibinacci Sequence 0..n
    Returns a `deque()` in reverse order
    where `seq[0]` is the largest int and
    `seq[-1] is the smallest int in the seq
    """

    seq = deque()
    seq.extendleft([0, 1])
    prv, cur, nxt = 1, 1, 0
    while cur < n:
        nxt = cur + prv
        prv = cur
        seq.appendleft(cur)
        cur = nxt
    return seq


def masked(mask, _for=0x9):

    """
    Masks `mask`, determining if the last
    digit of `mask` equals `_for`
    Returns bool
    """

    return mask & 0xF == _for


def solution(limit):

    """
    Finds the solution for Sept. 2019's
    Reformed Dev Challenge.
    Once found, prints output in proper format
    """

    start = timer()
    n = max([x for x in fib(limit) if masked(pow(x, 2)) if is_prime(x)])
    end = timer()
    print(f"pard68, Python 3, {n}, {end - start}, the yeetiest")


if __name__ == "__main__":
    limit = 9000000000000000000
    solution(limit)
