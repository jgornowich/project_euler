# import math
import time

def is_prime(number):
    if number == 2:
        return True

    if number % 2 == 0:
        return False

    # for i in range(2, int((math.sqrt(number)))+1):
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    FIND_PRIME = 10001
    # FIND_PRIME = 6

    value = 0
    x = 2

    start_time = time.time()

    while value < FIND_PRIME:
        # print 'Checking if ', x, ' is prime'
        if is_prime(x):
            print x, ' is prime'
            value += 1
        x += 1

    elapsed_time = time.time() - start_time
    print 'Time taken: ', elapsed_time, ' seconds'
