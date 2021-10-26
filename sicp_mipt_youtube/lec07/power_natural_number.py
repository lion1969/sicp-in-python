"""
a**n

pow(a,n) =
        1, if n = 0
        pow(a, n-1)*a, n > 0
"""


def pow(a: int, n: int) -> int:
    assert n >= 0 or a >= 0, "Agrh! Ouch!"
    return 1 if n == 0 else pow(a, n - 1) * a


print(pow(2, 30))
