def binary_search(table, search_value):
    begin = 0
    end = len(table) - 1
    while begin < end:
        middle = int((begin + end) / 2)
        if table[middle] >= search_value:
            end = middle
        else:
            begin = middle + 1
    return begin


if __name__ == '__main__':
    table = [1, 4, 5, 9, 12, 18, 20, 21, 27, 32, 35, 48, 49, 51, 54]
    search_value = 12

    position = binary_search(table, search_value)
    print("Found position: " + str(position + 1) + " has value " + str(table[position]))
