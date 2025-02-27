""" Basic Python: Reading Files, Loops, and Type Hints
Exercise 1: Write a function that reads a file and prints each line with its line number. Use type hints.
"""
# filename: str = "./../lab03-hashing/wordlist.txt"

def read_file_print (filename: str):
    with open (filename, "r") as fh:
        for line_number, line in enumerate(fh):
            print(line_number, line)

# Test
filename: str = "./../lab03-hashing/names.txt"
print("-------------------Exercise 1-------------------")
read_file_print(filename)
"""  Lists and Tuples
Exercise 2: Given a list of numbers, write a function that:
Appends 100 to the list
Inserts 50 at index 2
Pops the last element and returns it
"""
def list_operation(numbers: list) -> int:
    numbers.append(100)
    numbers.insert(2, 50)
    number: int = numbers.pop()
    return number
# Test
numbers = [3,23,5,6,2.3,7,5,10]
print("-------------------Exercise 2-------------------")
print(f"pop number is {list_operation(numbers)}")
print(f"list {numbers}")
"""
Exercise 3: Implement binary search on a sorted list.
"""
def binary_search(arr: list[list], value: int):
    right = len(arr) -1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            right = mid -1
        else:
            left = mid + 1
    return -1

# Test
nums = [1, 3, 5, 7, 9, 11]
index1 = binary_search(nums, 3)
index2 = binary_search(nums, 20)
# ternary expression for python
print("-------------------Exercise 3-------------------")
print(f"Index: {index1}, Result: {'not found' if index1 == -1 else 'found'}")
print(f"Index: {index2}, Result: {'not found' if index2 == -1 else 'found'}")

"""
Exercise 4: Demonstrate hashing in Python with a dictionary.
"""
# Simple hashing example using Python's built-in hash function
data = {"Alice": 25, "Bob": 30, "Charlie": 35}

# Hash values for each key
# print(f"Hash of 'Alice': {hash('Alice')}")
# print(f"Hash of 'Bob': {hash('Bob')}")
# print(f"Hash of 'Charlie': {hash('Charlie')}")
#
# # Retrieving values using hashing (simulated)
# key = "Alice"
# computed_hash = hash(key)  # Simulating internal dictionary lookup
# print(f"Retrieving {key} using its hash ({computed_hash}): {data[key]}")
print("-------------------Exercise 4-------------------")
"""
Exercise 5: Given a list of numbers, return a list with duplicates removed using a set.
"""
def removed_duplicate_list(lst: list) ->list:
    # nums_set = set ()
    # for num in lst:
    #     nums_set.add(num)
    # print(nums_set)
    # return list(nums_set)
    return list(set(lst))
# Test
print("-------------------Exercise 5-------------------")
lst =[2,4,6,8,1,6,8,2,4,5,10]
print(f"{removed_duplicate_list(lst)}")

"""
Exercise 6: Loop over a set and print elements.
"""
def loop_set(elements: set):
    for element in elements:
        print(element)

# Test
print("-------------------Exercise 6-------------------")
elements = {2,5,8,11,12,15}
loop_set(elements)
"""
Exercise 7: Count occurrences of words in a list.
"""
def count_words(words: list)-> dict[str : int]:
    dict_word = {}
    for word in words:
        if word not in dict_word:
            dict_word[word] = 1
        else:
            dict_word[word] += 1
    return dict_word

# Test
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print("-------------------Exercise 7-------------------")
print(count_words(words))

"""
Exercise 8: Loop through a dictionary.
"""
def loop_dict(data: dict):
    for key, value in data.items():
        print(f"{key}: {value}")

# Test
print("-------------------Exercise 8-------------------")
datas = {'apple': 3, 'banana': 2, 'orange': 1}
loop_dict(datas)

"""
Exercise 9: Implement a stack using a list.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        else:
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    # The peek method in the Stack class is used to retrieve (or "peek at")
    # the top element of the stack without removing it
    def peek(self):
        if not self.is_empty(): # Check if the stack is not empty
            return self.stack[-1]  # Return the top element (last element) without removing it
        else:
            print("Stack is empty!")
            return None

    def size(self):
        return len(self.stack)

    # to string
    def __str__(self):
        return f"Stack: {self.stack}"

# Test
print("-------------------Exercise 9------------------")
s = Stack()
s.push(10)
s.push(20)
s.push(50)
print(s.stack)  # output: [10, 20, 50]
print(s.pop())  # output: 50
print(s.stack)  # output: [10, 20]
print(s)  # output: Stack: [10, 20]
print(s.peek())  # Output: 20

