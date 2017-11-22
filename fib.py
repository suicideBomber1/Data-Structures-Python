def fib_rec(n):
    if n <= 2:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return a


print(fib_iter(4))
