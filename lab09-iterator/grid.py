class Grid:
    # way1
    # def __init__(self, rows, cols):
    #     self.rows = rows
    #     self.cols = cols
    #     # 2D
    #     self.grid = [[None for _ in range(cols)] for _ in range(rows)]
    #     self.current_row = 0
    #     self.current_col = 0
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     if self.current_row >= self.rows:
    #         raise StopIteration
    #
    #     value = self.grid[self.current_row][self.current_col]
    #
    #     # Next position (right to left by row, up to down by column)
    #     self.current_col += 1
    #     if self.current_col >= self.cols:
    #         self.current_col = 0
    #         self.current_row += 1
    #
    #     return value
    #
    # def display(self):
    #     """Prints the grid."""
    #     for row in self.grid:
    #         print(" ".join(map(str, row)))

    # way2
    def __init__(self):
        self.cells = dict()

    def __iter__(self):
        return iter(self.cells.items())



grid = Grid(3, 3)
# grid.display()

a = [1, 2, 3]
type(a)
x = iter(a)
type(a)


