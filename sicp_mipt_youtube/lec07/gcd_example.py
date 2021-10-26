def gcd_substraction(a: int, b: int) -> int:
    """
    Return Greatest Common Devisor.
    GCD =:
    a, if b = b
    gcd(a - b, b) if a > b
    gcd(a, b - a) if b > a
    :param a: int
    :param b: int
    :return: int
    """
    assert a >= 1 and b >= 1, "Argh!"
    if a == b:
        return a
    elif a > b:
        return gcd_substraction(a - b, b)
    else:  # a < b
        return gcd_substraction(a, b - a)


def gcd(a: int, b: int) -> int:
    """
    GCD(a, b) == GCD(b, a % b)
    Return Greatest Common Devisor.
    GCD =:
    a, if b = 0
    gcd(a - b, b) if a > b
    gcd(a, b - a) if b > a
    :param a: int
    :param b: int
    :return: int
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_cool(a: int, b: int) -> int:
    """
    :param a: int
    :param b: int
    :return: int
    """
    return a if b == 0 else gcd_cool(b, a % b)

print(gcd_substraction(36, 60))
print(gcd(36, 60))
print(gcd_cool(36, 60))