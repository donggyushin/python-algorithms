def fact(n: int) -> int:

    # Base case
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
