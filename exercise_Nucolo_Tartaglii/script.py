import sys


def puzzle(p, q):
    begin = 0
    end = q
    while begin < end:
        middle = int((begin + end) / 2)
        result = middle ** 3 + p * middle
        if result == q:
            return middle
        elif result > q:
            end = middle
        else:
            begin = middle + 1

    return 'NIE'


if __name__ == '__main__':
    max = int(input())
    for var in list(range(max)):
        pq = input().split(" ")
        p = int(pq[0])
        q = int(pq[1])
        print(str(puzzle(p,q)))
