from time import time
from timeit import default_timer

LIMIT = 9000000000000000000

def square_hexidecimal_ends_with_9(number):
    """ Return whether the given number's square ends with 0x9 """
    return (number * number) & 0xf == 0x9

def get_special_fibonacci_numbers_under(limit):
    """
    Return a list of fibonacci numbers whose square ends with 0x9
    The list stops at the given limit
    """
    numbers = []
    previous, current = 1, 1
    while current < limit:
        if square_hexidecimal_ends_with_9(current):
            numbers.append(current)
        previous, current = current, previous + current

    return numbers

def is_prime(number):
    """ Returns whether the given number is prime """
    if number <= 1 or not number % 2:
        return False
    return all(number % num for num in range(3, int(number**0.5) + 1, 2))

def find_answer_search_fibonacci():
    """ Count up fibonacci numbers to find the answer """
    fibonacci_numbers = get_special_fibonacci_numbers_under(LIMIT)
    for number in reversed(fibonacci_numbers):
        if square_hexidecimal_ends_with_9(number) and is_prime(number):
            return number

if __name__ == '__main__':
    start = default_timer()
    answer = find_answer_search_fibonacci()
    end = default_timer()

    print(f'Pathfinder216, Python, {answer}, {(end - start) * 1000}, Simple optimized')
