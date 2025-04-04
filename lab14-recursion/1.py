def fact(n):
    global a
    if n == 0:
        return 1
    y = n * fact(n-1)
    return y
a = 12
z = fact(5)

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

print(f"use is_even",is_even(2))
print(f"use is_odd",is_odd(2))