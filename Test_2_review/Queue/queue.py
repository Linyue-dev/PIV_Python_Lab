class Queue:

    def __init__(self, data):
        self.data = data
    def put(self):
        self.data.pop(0)

    def get(self):
        self.data.appemd()