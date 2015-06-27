import math

def is_prime(number):
    for i in range(2, int(math.ceil(math.sqrt(number)))):
        if number % i == 0:
            return False
    return True

def check_for_prime_factors(number):
    """
    The simplest, inefficient primality test is trial division from 2 to n-1

    However, its better to eliminate all impossible primality candidates, knowing that any
    divisors greater than sqrt(n) because after this point the candidates just flip around
    and repeat themselves.

    Then we can eliminate all even numbers from this subset as they are by definition divisible
    by 2 and thus can't be prime numbers.
    """
    subset = []

    # sort out the things we know can't be prime
    for i in range(3, int(math.ceil(math.sqrt(number)))):

        # even numbers above 2 can't be prime
        if i % 2 == 0:
            continue

        # check all the rest for primality
        if not is_prime(i):
            continue

        # now check that its a prime factor of the given number
        if number % i == 0:
            subset.append(i)

    return subset


if __name__ == '__main__':
    # INPUT = 13195
    INPUT = 600851475143

    output = check_for_prime_factors(INPUT)

    print output
    print output[-1]
