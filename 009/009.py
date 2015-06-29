def sum_pythagorean_triplet(triplet):
    sum_triplet = triplet[0] + triplet[1] + triplet[2]
    return sum_triplet


def create_pythagorean_triplet(m, n):
    """
    Given two values m < n a pythagorean triplet can be created as follows:
        a = n**2 - m**2
        b = 2nm
        c = n**2 + m**2
    """
    a = n ** 2 - m ** 2
    b = 2 * n * m
    c = n ** 2 + m ** 2

    answer = (a, b, c)

    return answer


if __name__ == '__main__':

    MAX_VALUE = 60

    # test_set = (1, 3, 9)
    for (m, n) in [(m, n) for m in range(1, MAX_VALUE) for n in range(1, MAX_VALUE)]:

        # enforce the inequality
        if n < m:
            continue

        # print 'Creating triplet for (m,n) = (', m, ',', n, ')'
        triplet = create_pythagorean_triplet(m, n)
        print 'Sum of triplet', triplet, ' is ', sum(triplet)

        if sum(triplet) == 1000:
            print("FOUND IT")
            break;

    # Now find the product of the triplet
    answer = triplet[0] * triplet[1] * triplet[2]
    print 'Its product is', answer
