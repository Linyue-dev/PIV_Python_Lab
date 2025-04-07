from typing import Callable, TypeVar

A = TypeVar("A")
def filter_list_h(predicate: Callable[[A], bool], xs: list[A], index: int) -> list[A]:
    if index == len(xs):
        return []

    tmp = filter_list_h(predicate, xs, index + 1)
    if predicate(xs[index]):
        return [xs[index]] + tmp
    else:
        return tmp


# ===================================sum list========================================
a = [1, 3, 2, 6, 7, 4]

# def sum(a: list):
#     if len(a) == 0:
#         return 0
#     item = a.pop()
#     return item + sum(a)
# print(sum(a)) # 23

def sum_recursive(a: list, index=0):
    if index == len(a):
        return 0
    return a[index] + sum_recursive(a, index + 1)

print(sum_recursive(a)) # 23
print(f"list still:", a)  # Still [1, 3, 2, 6, 7, 4]


# ===================================find max number of list========================================
def find_max_number(a:list):
    if len(a) == 1:
        return a[0]
    max_of_rest = find_max_number(a[1:])
    if a[0] > max_of_rest:
        return a[0]
    else:
        return max_of_rest
print(f"use list as parameter:", find_max_number(a))

# def find_max(a:list, i:int =0):

def maxf(a: list, i: int):
    if i < len(a) - 1:
        return a[i]
    tem = maxf(a, i+1)
    if tem > a[i]:
        return tem
    else:
        return a[i]
print(f"use list and int two parameters:",find_max_number(a))

print(f"use max(a):", max(a))

# ===================================symmetry========================================
a: str = "anna"
def symmtry(a):
    if len(a) <= 1:
        return True
    if a[0] != a[-1]:
        return False
    return symmtry(a[0:-1])

print(symmtry(a))
