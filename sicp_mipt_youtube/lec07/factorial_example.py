def f(n: int):
    """
    Вычисляет факториал n.
    :type n: int
    """
    assert n >= 0, "Argh!"
    if n == 0:
        return 1
    return f(n - 1) * n


n = int(input("Enter N to count Factorial: "))
print("Factorial(", n, ") =", f(n))
print(f.__doc__)
