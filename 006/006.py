import timeit

def sum_of_squares(number):
    ans = 0
    for i in range(1, number + 1):
        ans += i ** 2
    return ans


def square_of_sums(number):
    ans = 0
    for i in range(1, number + 1):
        ans += i
    return ans ** 2

if __name__ == '__main__':
    VALUE = 100

    # experiment with timing functions and code blocks
    start_time = timeit.default_timer()
    print square_of_sums(VALUE) - sum_of_squares(VALUE)
    print 'function-way took: ', timeit.default_timer() - start_time

    # one liner way of doing this, which is about twice as fast as the above method
    start_time = timeit.default_timer()
    print sum(range(1, VALUE+1))**2 - sum(x**2 for x in range(1, VALUE+1))
    print 'oneline-way took: ', timeit.default_timer() - start_time