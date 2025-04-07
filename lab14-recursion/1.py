def fact(n):
    global a
    if n == 0:
        return 1
    y = n * fact(n-1)
    return y
a = 12
z = fact(5)

# 1       0   RESUME  0
# 2       2   LOAD_FAST   2(index)
#         4   LOAD_GLOBAL
#         1(NULL + len)
#         14 LOAD_FAST    1(xs)
#         16  CALL    1
#         24  COMPARE_OP  40( ==)       <---if
#         28  POP_JUMP_IF_FALSE   2(to 34)
# 3       30  BUILD_LIST  0
#         32  RETURN_VALUE
# 5 >>    34  LOAD_GLOBAL 3(NULL + filter_list_h)
#         44  LOAD_FAST   0(predicate)
#         46  LOAD_FAST   1(xs)
#         48  LOAD_FAST   2(index)
#         50  LOAD_CONST  1(1)
#         52  BINARY_OP   0(+)
#         56  CALL    3
#         64  STORE_FAST  3(tmp)
#         6   66  PUSH_NULL
#         68  LOAD_FAST   0(predicate)
#         70  LOAD_FAST   1(xs)
#         72  LOAD_FAST   2(index)
#         74  BINARY_SUBSCR
#         78  CALL    1
#         86  POP_JUMP_IF_FALSE   9(to 106)
#         7   88  LOAD_FAST   1(xs)
#         90  LOAD_FAST   2(index)
#         92  BINARY_SUBSCR
#         96  BUILD_LIST  1
#         98  LOAD_FAST   3(tmp)
#         100 BINARY_OP   0(+)
#         104 RETURN_VALUE
# 9 >>    106    LOAD_FAST   3(tmp)
#         108 RETURN_VALUE
# ====================================================================
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

print(f"use is_even", is_even(2))
print(f"use is_odd", is_odd(2))