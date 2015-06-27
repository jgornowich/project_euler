def compute_fibonacci_sequence(max_number):
    """Find the fibonacci sequence up to some max number"""

    value = 0
    sequence = [1, 2]

    while value < max_number:
        value = sequence[-1] + sequence[-2]
        sequence.append(value)

    if value > max_number:
        sequence.pop()

    return sequence


def sum_even_fibonacci_sequence(sequence):
    """Sum the even numbers of the given fibonacci sequence"""

    answer = 0
    for i in sequence:
        if i % 2 == 0:
            answer += i

    return answer


if __name__ == '__main__':
    MAX_VALUE = 4000000
    sequence = compute_fibonacci_sequence(MAX_VALUE)
    print sequence
    answer = sum_even_fibonacci_sequence(sequence)
    print answer
