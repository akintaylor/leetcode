# tail recursion
def add_zero_to_n(n, total=0):
    if n == 0:
        return total
    return add_zero_to_n(n-1, total+n)


# normal recursion
def add_zero_to_n(n):
    if n == 0:
        return 0
    return n + add_zero_to_n(n - 1)


# while
def add_zero_to_n(n):
    total = 0
    while (n > 0):
        total += n
        n -= 1

    return total
