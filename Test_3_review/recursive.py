"""Recursion
Factorial
In mathematics, the factorial of a number n is the product of all the numbers 1, 2, .. n:

n! = 1 * 2 * ... * n
For example, the factorial of 5 is

5! = 5 * 4 * 3 * 2 * 1 = 120
There is another way to think about this 5!. Consider this:

5! = 5 * 4 * 3 * 2 * 1
   = 5 * (4 * 3 * 2 * 1)
   = 5 * 4!
This gives us a "recursive" definition for factorial:

n! = n * (n - 1)!
Demo: code the factorial function
Code a recursive method that implements factorial:

First attempt:"""
from optparse import Option
from typing import TypeVar, Callable, Optional


def fact(n: int):
   return n * fact(n - 1)
"""We will refer to function calls like fact(n - 1) as recursive calls.

Do you see any problem with this function?

Second attempt:

We are missing an important piece of information. The factorial of 0 is defined to be one 1. The full mathematical definition is:

0! = 1
n! = n * (n - 1)!
which we can code as:"""

def fact(n: int):
   if n == 0:
      return 0
   else:
      return n * fact(n - 1)
"""Better? There is now an execution path that will not make a recursive call. We refer to this as a base case.

Ingredients of recursion
A recursive call makes a function recursive and a base case is what makes it stop!

A recursive call without a base case will result in "infinite" recursion, a recursive function that will repeat "forever". Since we don't have infinite computing resources, we will run out of call stack space and a RecursionError: maximum recursion depth exceeded will be thrown.

There is an important rule about recursive calls:

"Every recursive call must approach the base case."

For example, the call fact(-1) will not terminate in the above function, since each subsequent call will be a negative number.

Exercise: Even's and Odd's
Does the following recursive function lead to infinite recursion:"""

def is_even(n: int) -> bool:
    if n == 0:
        return True
    else:
        return is_even(n - 2)
# If it does, can you fix this method?
#
# Please, please, don't use is_even(n) in a real program. In fact, most of the things we do in this part of the course is to learn recursion from examples we know we can do non-recursively. Later, we will see some interesting recursion examples and talk about when recursion is the right programming technique to use.
#
# Optional: Even more even and odds
# Here's a an odd way to determine if a number is even or odd:

def is_even(n: int):
    if n == 0:
        return True;
    else:
        return is_odd(n - 1)

def is_odd(n: int):
    if n == 0:
        return False
    else:
        return is_even(n - 1)
"""
We call these two methods mutually recursive. How do these two methods work together to figure out if a number is even or odd?

How do we know this terminates for n >= 0?

Tracing recursion
Trace execution of fact(5).
fact(5) = 5 * fact(4)
              v--------v
              4 * fact(3)
                  v---------v
                  3 * fact(2)
                      v--------v
                      2 * fact(1)
                          v---------v
                          1 * fact(0)
                              v-----v
                              1
                          1 * 1
                          v---v
                      2 * 1
                      v---v
                 3 * 2
                 v---v
             4 * 6
             v---v
         5 * 24
         v----v
         120
Designing recursive functions.
Lets design a recursive function that will compute the sum of an list.

We start with an idea for a method. We will design our function with a parameter index:
def sum(xs: list[A], index: int) -> int:
Here is a description of what the sum(xs, index) computes: it returns the sum of the elements in xs from index to length - 1.

From this description, we can think of our recursive call as adding the value at xs[index] to the sum of the remaining elements in the list, i.e.: xs[index + 1] + xs[index + 2] + ... + xs[xs.length - 1].
def sum(xs: list[int], index: int):
    return xs[index] + sum(xs, index + 1)
This is obviously infinite recursion, so let's add a base case. Aside from needing to stop recursion

"""
def sum(xs: list[int], index: int):
    if index == len(xs):
        return 0
    else:
        return xs[index] + sum(xs, index + 1)
"""Reasoning about termination: each recursive call increases the index by 1 which steps closer and closer to the length of the list at which point we hit the base case.
Exercise: implement a max method recursively
Good:"""
A = TypeVar("A")
def max(xs: list[A], index: int):
    if index == len(xs) - 1:
        return xs[index]

    tmp = max(xs, index + 1)
    if tmp > xs[index]:
        return tmp
    else:
        return xs[index]
"""Bad:"""

def max(xs: list[A], index: int):
    if index == len(xs) - 1:
        return xs[index]

    if max(xs, index + 1) > xs[index]:
        return max(xs, index + 1)
    else:
        return xs[index]
"""Why?

Private helper methods
Since calling the method max is awkward with the second argument we can restructure like this:"""

def max(xs: list[A]) -> A:
    return max_h(xs, 0)

def max_h(xs: list[A], index: int):
    if index == len(xs) - 1:
        return xs[index]

    tmp = max_h(xs, index + 1)
    if tmp > xs[index]:
        return tmp
    else:
        return xs[index]
"""Exercise: implement a is_palindrome method recursively
A palindrome is a word (or sentence) whose spelling is the same when read forwards or backwards. Examples of palindromes: "racecar", "taco cat", "tattarrattat".
"""
def is_palindrome(word: str, left: int, right: int):
    if left >= right:
        return True

    if word[left] == ' ':
        return is_palindrome(word, left + 1, right)

    if word[right] == ' ':
        return is_palindrome(word, left, right - 1)

    if word[left] != word[right]:
        return False

    return is_palindrome(word, left + 1, right - 1)

"""The recursive structure of lists
An list sub-list is a piece of an original list. When we do recursion on an list we are working on smaller and smaller sublists.

Sum, etc… the sublist gets smaller on one end.
Palindrome, the sublist gets smaller on both ends
DRAWING in class

Exercise Binary Search
Write method binary_search(..) that will return the position of a value x within an list xs or -1 if it's not in the list using recursion and binary search.

How do we know recursion terminates with recursive binary search? Use the word slice in your answer."""

def binary_search(xs: list[A], x: A) -> int:
    return binary_search_h(xs, x, 0, len(xs) - 1)

# recursive "helper" function
def binary_search_h(xs: list[A], x: A, low: int, high: int) -> int:

    if low > high:
        return -1

    mid = (low + high) // 2

    if xs[mid] == x:
        return mid

    if xs[mid] > x:
        return binary_search_h(xs, x, low, mid - 1)
    else:
        return binary_search_h(xs, x, mid + 1, high)
data = [1, 5, 7, 9, 10, 15, 16]
print(binary_search(data, 5, 0, len(data)))
"""Exercise: recursive filter
Code the filter_list function recursively

Version 1:
"""
def filter_list(predicate: Callable[[A], bool], xs: list[A]) -> list[A]:
    return filter_list_h(predicate ,xs, 0)

def filter_list_h(predicate: Callable[[A], bool], xs: list[A], index: int) -> list[A]:
    if index == len(xs):
        return []

    tmp = filter_list_h(predicate, xs, index + 1)
    if predicate(xs[index]):
        return [xs[index]] + tmp
    else:
        return tmp
"""pros:

it's based on the pattern we've seen before, so we can understand it.
cons:

we make a ton of lists along the way… this is bad
Version 2:"""

def filter_list(predicate: Callable[[A], bool], xs: list[A]) -> list[A]:
    accumulator: list[A] = []
    filter_list_h(predicate ,xs, 0, accumulator)
    return accumulator

def filter_list_h(predicate: Callable[[A], bool], xs: list[A], index: int, accumulator: list[A]):
    if index == len(xs):
        return

    if predicate(xs[index]):
        accumulator.append(xs[index])

    filter_list_h(predicate, xs, index + 1, accumulator)
"""pros:

much faster! Remember that the non-recursive version is better, but soon enough you'll see examples where recursion is beneficial.
cons:

more parameters!
Exercise: mergesort
MergeSort is a recursive sorting algorithm that is efficient. It's especially useful when sorting data stored in structures that have slow random access, ex: files, etc…

Before we tackle the sort algorithm, let's implement the method merge. It does most of the work in the algorithm!

Merge
A merge takes two sorted list sublists and combines them into a third sublist in such a way that the elements are sorted.

DRAWING ON BOARD IN CLASS

The setup is based on how we plan on calling merge(..) from within the sort:

The two sublists are next to each other in the list src[left..mid] and src[mid+1..right]. We call them contiguous.
Precondition 1: left < mid and mid + 1 < right.
Precondition 2: sublist src[left..mid] and src[mid+1..right] are sorted ascending.
The merged elements are put into dst."""
def merge(src: list[A], low: int, mid: int, high: int, dst: list[Optional[A]]):
    """Merge src[low:mid] with src[mid+1:high] into dst[low:high].
       Assumes that src[low:mid] and src[mid+1:high] are individually sorted when this is called"""

def merge(src: list[A], low: int, mid: int, high: int, dst: list[Optional[A]]):
    """Merge src[low:mid] with src[mid+1:high] into dst[low:high].
       Assumes that src[low:mid] and src[mid+1:high] are individually sorted when this is called"""
    i: int = low
    j: int = mid + 1

    for k in range(low, high + 1):
        if i > mid:
            dst[k] = src[j]
            j += 1
        elif j > high:
            dst[k] = src[i]
            i += 1
        elif src[i] < src[j]:
            dst[k] = src[i]
            i += 1
        else:
            dst[k] = src[j]
            j += 1

"""Sort"""
def mergesort(xs: list[A]):
    buffer: list[A] = [None] * len(xs)
    mergesort_h(xs, 0, len(xs) - 1, buffer)


def mergesort_h(xs: list[A], low: int, high: int, buffer: list[Option[A]]):
    if low >= high:
        return

    # sort the two evenly divied sublists
    mid: int = (low + high) // 2
    mergesort_h(xs, low, mid, buffer)
    mergesort_h(xs, mid + 1, high, buffer)

    # copy the sub-lists into the buffer
    for i in range(low, high + 1):
        buffer[i] = xs[i]

    # merge back into xs, so now xs[low:high] is now sorted
    merge(buffer, low, mid, high, xs)

"""Trace
Colored output from the sample can be found here https://github.com/ianclement/tracelist"""