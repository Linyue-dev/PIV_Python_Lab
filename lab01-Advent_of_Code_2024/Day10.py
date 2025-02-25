class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

name: str
symbol: str
compare = {
    ")": "(",
    "]": "[",
    ">": "<"
}
opening_chrs = ("(", "[", "<", "{")
test_line = "{([(<{}[<>[]}>{[]{[(<()>"
stack = Stack()
for char in test_line:
    if char in opening_chrs:
        stack.push(char)
    else:
        from_stack = stack.pop()
        if compare[char] != from_stack:
            print("not good")
            break

# stack = new Stack()
# paired = {'{':'}','[':']','(':')','>':'>'}
