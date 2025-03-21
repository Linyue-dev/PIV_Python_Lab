# ===============================================================
# def is_even(n):
#     return n % 2 == 0
#
# def is_odd(n):
#     return n % 2 != 0
#
# a = [1, 2, 3, 4, 5, 6]  # Example list
#
# ans = input("even or odd?").strip().lower()
#
# predicate = is_even if ans == "even" else is_odd
# nums = [i for i in a if predicate(i)]  # List comprehension for efficiency
#
# print(nums)

# ===============================================================

# ans = list()
# for i in ans:
#     if predicate(i):
#         ans.append(i)
#     # return ans

# ===============================================================
""" 
print the games that are have a review of \>25 without using a for-loop 
"""
my_games = [
    (27, "Great game 1"),
    (20, "Average game 1"),
    (10, "Bad game 1"),
    (12, "Bad game 2"),
    (7, "Terrible game"),
    (25, "Average game 1"),
    (49, "Best game ever")
]
# filter(predicate : Callable[[A], bool], Iterable[[A]]) -> Iterable[A]
def good_game(game):
    return game[0] >= 25

print(list(filter(good_game, my_games)))
