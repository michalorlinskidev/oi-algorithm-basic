def power(a, n):
    if n == 1:
        return a
    return a * power(a, n - 1)


def quick_power(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        s = quick_power(a, n/2)
        return s * s
    else:
        a * power(a, n - 1)


if __name__ == '__main__':
    print(power(3,4))
    print(quick_power(3,4))