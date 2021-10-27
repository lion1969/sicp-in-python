"""
a**n

pow(a,n) =
        1, if n = 0
        pow(a, n-1)*a, n > 0
"""


def pow(a: float, n: int) -> int:
    assert n >= 0, "Agrh! Ouch!"

    if n == 0:
        return 1
    elif n % 2 == 1:  # Нечётная степень
        return pow(a, n - 1) * a
    else:  # Чётная степень
        return pow(a ** 2, n // 2)


print(pow(2, 30))
