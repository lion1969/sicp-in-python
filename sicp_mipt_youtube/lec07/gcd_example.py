def gcd(a: int, b: int):
    """
    Return Greatest Common Devisor
    :param a: int
    :param b: int
    :return: int
    """
    assert a >= 1 and b >= 1, "Argh!"
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else: # a < b
        return gcd(a, b - a)


print(gcd(36, 60))
