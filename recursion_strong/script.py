def strong(a):
    if a == 2:
        return a
    return a * strong(a - 1)


if __name__ == '__main__':
    print(strong(5))