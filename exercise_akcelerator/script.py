def binary_search_begin(table, search):
    begin = 0
    end = len(table) - 1
    while begin < end:
        middle = int((begin + end) / 2)
        if table[middle] >= search:
            end = middle
        else:
            begin = middle + 1
    return binary_search_return_value(table, begin, search)


def binary_search_end(table, search):
    begin = 0
    end = len(table) - 1
    while begin < end:
        middle = int((begin + end + 1) / 2)
        if table[middle] <= search:
            begin = middle
        else:
            end = middle - 1
    return binary_search_return_value(table, begin, search)


def binary_search_return_value(table, found, search):
    if table[found] == search:
        return found
    else:
        return -1


if __name__ == '__main__':
    table_size = int(input())
    table = input().split(" ")
    table = [int(i) for i in table]
    queries_size = int(input())
    for var in list(range(queries_size)):
        query = int(input())
        begin = binary_search_begin(table, query)
        end = binary_search_end(table, query)
        if begin == -1:
            print(0)
        else:
            print(end - begin + 1)