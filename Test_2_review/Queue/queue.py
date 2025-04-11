class Queue:

    def __init__(self, data):
        self.data = data
    def put(self):
        self.data.appemd()

    def get(self):
        self.data.pop(0)