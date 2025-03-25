from typing import TypeVar

A = TypeVar("A")
# def filter_list(predicate: Callable[[A],bool], data: list[A]) -> list[A]:
def filter_list(predicate, data: list[A]) -> list[A]:
    # predicate Callable
    # Callable[[A], bool]
    result = []
    for a in data:
        if predicate(a):
            result.append(a)
    return result

def predicate(x) -> bool:
    return type(x) is str

data: list[int] = [3, 4, "3", "4"]
result = filter_list(predicate, data)
print(result)


# ==========================
def is_not_comment(line):
    # return not line.startswith("#")
    line.lstrip()

def map_list(changeType, data) ->list:
    return [changeType(item) for item in data]

def changeType(d:str) -> int:
    try:
        num = int(d)
        return num
    except ValueError:
        print("d cannot convert to integer")
        return 0

# # type is str change to int
data = ["3", "5", "7"]
filter_data = [3,5,7]  # Output: [3, 5, 7]
print(filter_data)

# ===============================================
# str.isgigit() str.rstip()
test_data = ["3\n", "5\n", "6\n", "abc\n", "16\n"]
# Output ["3","5","6","abc","16"]
# Output ["3","5","6","16"]
# map_list(int, filter_list(str.isdigit, map_list(str.rstrip,fh)))
# for n in map(int, map(str.rstrip, fh)): default read the file
# any(predicate, data)->data
# all(is_even, range(1, 10))