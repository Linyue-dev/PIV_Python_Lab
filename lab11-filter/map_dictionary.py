# Exercise:
# code a function map_dict_value that maps the values of the dictionary using
# the provided mapping function

def map_dict_value(f, data: dict) -> dict:
    results = {}  # dict
    for k, v in data.items():
        results[k] = f(v)
    return results

# def map_dict_value(f:Callable[[A] -> B], data: dict[K,A]) -> dict[A,B]:
#     results = {}  # dict
#     for k, v in data.items():
#         results[k] = f(v)
#     return results

data = dict(zip("abcsdeg",range(10, 100)))
d = dict(zip("abcsdeg",range(7)))

y = map_dict_value(lambda x: x+1, d)
print(y)
# Question: What about a map_dict_key or even map_dict_item. Any issue?

d = dict[("a", 2), ("b", 1), ("c", 5), ("z",34), ("a", 5), ("z", 4)]
# d = dict([("a", 2), ("b", 1), ("c", 5), ("z",34), ("a", 5), ("z", 4)])
print(f"d -> ", d)

#
# def dict_from_list_with(f: Callable[[B,B], B], kvs: list[tuple[A,B]]) ->dict[A,B]:
def dict_from_list_with(f: Callable, kvs: list) ->dict:
    """Create a dict from a list with a combining function f"""

    results = {}
    for k, v in kvs:
        if k in results:
            tem = results[k]
            new_v = f(tem, v)
            results[k] = new_v
        else:
            results[k] = v

    return results


l= [("a", 2), ("b", 1), ("c", 5), ("z", 34), ("a", 5), ("z", 4)]
ll = [()]
dict_from_list_with(lambda x, y: x+y, l)

# x = map(f: Callable[[A],B], l: Iterable[A]) -> Iterable[B]
# x = list(map())
# Iterable --- important