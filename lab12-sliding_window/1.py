from typing import Callable, Optional, TypeVar

# Exercise
# List a integers
# sub-list of length k
a = [1, 2, 7, 13, 20, 2, 8]
k = 3
# [1, 2, 7]
# [2, 7, 13]
# [3, 13, 20]
# [13, 20, 2]
# [20, 2, 8]
# get maximum sub list sum
# ====================================Way1====================================
sub_list = []
for i in range(len(a)-k+1):
    sum1 = a[i] + a[i+1] + a[i+2]
    sub_list.append(sum1)

print(max(sub_list))
# ====================================Way2====================================
# max = -math.inf
# s = 0
# for i in range(0, len(a)-k+1):
#     max_sum = sum(a[i:i+k])
#     if max_sum > max:
#         max = max_sum
# print(s)
# ====================================Way3====================================
# s = 0
# def foo(n_add, n_remove, s):
#     s = s + n_add
#     if n_remove is not None:
#         s = s - n_remove
#     return s

# for i in range(len(a)):
#     if i < k:
#         s = foo(a[i], None, s)
#         sub_list.append(s)
#     else:
#         # print(s)
#         s = foo(a[i], a[i-k], s)
#         sub_list.append(s)
#
# print(max(sub_list))

# ====================================Way4 foo() as parameter do callable function
def foo(n_add, n_remove, s):
    s = s + n_add
    if n_remove is not None:
        s = s - n_remove
    return s

A = TypeVar("A")
B = TypeVar("B")
def sliding_window(a: list[A], k: int, s:B, foo: Callable[[A,(Optional)[A], B], B]) ->list[B]:
    result = []
    for i in range(len(a)):
        if i < k:
            s = foo(a[i], None, s)
        else:
            result.append(s)
            s = foo(a[i], a[i - k], s)
    result.append(s)
    return result
result = sliding_window(a, 3, 0, foo)
print(max(result))







