def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_sequence = [0]
    a, b = 0, 1

    for _ in range(1, n):
        fib_sequence.append(b)
        a, b = b, a + b

    return fib_sequence