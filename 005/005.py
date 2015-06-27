def divisible_by_range(number, max):
    """
    Its most efficient to search for divisibility backwards because this is the highest
    probability of failure
    """
    for i in range(max, 1, -1):
        if number % i != 0:
            return False
    return True


if __name__ == '__main__':
    step = 20
    i = 0
    # not ideal to use this while forever loop, but works for now
    while True:
        # print i
        i += step

        if divisible_by_range(i, step):
            print 'Got it, ', i
            break
