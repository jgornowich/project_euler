# import itertools
import sys

def is_palindromic_number(number):
    as_string = str(number)
    if as_string[::] == as_string[::-1]:
        return True

def get_product(first,second):
    return first*second

if __name__ == '__main__':
    MAX_VALUE = 999
    results = []
    for i in range(MAX_VALUE,1,-1):
        for j in range(MAX_VALUE,1,-1):
            if is_palindromic_number(get_product(i,j)):
                results.append(get_product(i,j))

    print max(results)


    # Experiment with other ways to iterate in Python
    #for i, j in zip(range(MAX_VALUE,1,-1), range(MAX_VALUE,1,-1)):
    #for i, j in itertools.product(range(MAX_VALUE,1,-1), range(MAX_VALUE,1,-1)):
    #for (i, j) in [(i, j) for i in range(MAX_VALUE, 1, -1) for j in range(MAX_VALUE, 1, -1)]:
        # print 'i =', i, ', j = ', j
        # if is_palindromic_number(get_product(i, j)) is True:
        #     print str(get_product(i, j))
        #     break
