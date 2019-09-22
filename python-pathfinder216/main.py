from time import time

LIMIT = 9000000000000000000

def square_hexidecimal_ends_with_9(number):
    return (number * number) & 0b1111 == 0x9

def get_prime_fibonacci_numbers_under(limit):
    numbers = []
    previous = 0
    current = 1
    while current < limit:
        if is_prime(current):
            numbers.append(current)
        current += previous
        previous = current - previous

    return numbers

def is_prime(number):
    """ Assumes number is greater than 1 """
    return all(number % num for num in range(2, int(number**0.5) + 1))

if __name__ == '__main__':
    start = time()

    prime_fibonacci_numbers = get_prime_fibonacci_numbers_under(LIMIT)
    for number in reversed(prime_fibonacci_numbers):
        if square_hexidecimal_ends_with_9(number):
            print(f'Found the answer: {number}')
            break

    end = time()
    print(f'Finished in: {end - start} seconds')
