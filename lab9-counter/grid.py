class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # self.end = (rows, cols)
        # self.start = (0, 0)
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def __iter__(self):
        return self

    def __next__(self):
        pass





