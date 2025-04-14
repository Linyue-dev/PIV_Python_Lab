# def filter_list(pred, xs:list) -> list:
#     return filter_list_h(pred, xs, 0)
#
# def filter_list_h(pred, xs, index):
#     if index == len(xs):
#         return []
#     temp = filter_list_h(pred, xs, index + 1)
#     if pred(xs[index]):
#         return [xs[index]] + temp
#     else:
#         return temp


xs = [1, 2, 3, 4]


def filter_list(pred, xs:list) -> list:
    acc = list()
    filter_list_h(pred,xs, acc, 0)
    return acc

def filter_list_h(pred, xs,acc, index):
    if index == len(xs):
        return []
    if pred(xs[index]):
        acc.append(xs[index])
    filter_list_h(pred, xs, acc, index + 1)
