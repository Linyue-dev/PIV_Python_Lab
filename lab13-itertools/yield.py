"""
The yield keyword is used to return a list of values from a function
When you call a function with yield keyword(s), the return value will be a list of values, one for each yield.
"""

def gen_func(m):
    for i in range(m):
        yield i  # Produces values one at a time

def id_gen(start):
    while True:
        yield start
        start += 1

