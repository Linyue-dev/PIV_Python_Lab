# def plus1(x:int) -> int:
#     return x + 1
# 1. Print all of these numbers multiplied by 7:[3, 5, 7,1 , 2, 3, 7]
import re

num = [3, 5, 7, 1, 2, 3, 7]
print(map(lambda x: x * 7, num))


# 2. Print all lines of source_code contain the COPYTO instructon.
source_code = open("ex1.hrm").readline()
print(filter(lambda line: re.search("^\s*COPYs+", line), source_code))
print(filter(lambda line: "COPYTO" in line, source_code))

# 3. Print all the games that have a rating below 10 or above 40

# print(filter(lambda , my_games))



my_games = [
    (27, "Great game 1"),
    (20, "Average game 1"),
    (10, "Bad game 1"),
    (12, "Bad game 2"),
    (7, "Terrible game"),
    (25, "Average game 1"),
    (49, "Best game ever")
]
def map_list(f, xs: list) ->list:
    ys: list = []
    for x in xs:
        ys.append(x)
    return ys
