class Stack:
    def __init__(self,data):
        self.data = data
    def pop(self) -> any:
        return self.data.pop(-1)

    def push(self):
        self.data.append()
