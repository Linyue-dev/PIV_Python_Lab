from typing import Callable, TypeVar

A = TypeVar("A")
B = TypeVar("B")
def map_list(key:Callable[[A],B],data:list[A])->list[B]:
    output = list()
    for d in data:
        new = key(d)
        output.append(new)
    return output

a = ["1", "2", "3"]
b = map_list(int, a)

# ===============================2========================
def sqyare(a:str) ->int:
    return int(a) ** 2
b = map_list(sqyare, a)