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
    MAX_PRIME_VALUE = 2000000

    value = 2
    answer = 0
    while value < MAX_PRIME_VALUE:
        if(is_prime(value)):
            answer += value
        value += 1

    print answer