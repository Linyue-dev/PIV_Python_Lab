l1 = [3,2,7,4]
l2 = [1,2,3]

def all_elements(l1: list, l2: list) -> set:

    set1  = set()
    set2  = set()
    for element in l1:
        set1 .add(element)

    for element in l2:
        set2.add(element)

    set1.update(set2)
    return set1
set = all_elements(l1,l2)
print(set)