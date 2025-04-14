def binary_search(l: list, start, stop, value) -> bool:
    while True:
        if start > stop:
            return False
        m = (start + stop) // 2
        if value == l[m]:
            return True
        elif value > l[m]:
            start = m + 1
        else:
            stop = m - 1

def binary_search_recursion(l:list, start, stop, value):
    if start > stop:
        return -1
    m = (start+stop) // 2
    if l[m] == value:
        return m
    elif l[m] < value:
        return binary_search_recursion(l, m + 1, stop, value)
    elif l[m] > value:
        return binary_search_recursion(l, start, m - 1, value)

data:list= [3, 6, 7, 9, 23, 35, 43, 45,65, 70, 101]
print(binary_search(data, 0, len(data), 23))
# print(binary_search_recursion(data, 0, len(data), 23))

