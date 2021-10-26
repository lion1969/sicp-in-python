"""
a**n

pow(a,n) =
        1, if n = 0
        pow(a, n-1)*a, n > 0
"""


def pow(a: float, n: int) -> int:
    assert n >= 0 , "Agrh! Ouch!"
    return 1 if n == 0 else pow(a, n - 1) * a


print(pow(2.00000, 30))
