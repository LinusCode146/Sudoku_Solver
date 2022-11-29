from typing import List


class SudokuSolver:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.numbers = {*range(1, 10)}

    def numbers_from_row(self, row):
        return self.numbers - {*self.grid[row]}

    def numbers_from_column(self, column):
        return self.numbers - {row[column] for row in self.grid}

    def numbers_from_box(self, row, column):
        return self.numbers - {self.grid[i//3 + (row//3)*3][i%3 + (column//3)*3] for i in range(0, 9)}

    def possible_values(self, row, column):
        return self.numbers_from_box(row, column).intersection(self.numbers_from_row(row), self.numbers_from_column(column))

    def solve(self):
        empty = None
        for i, row in enumerate(self.grid):
            if 0 in row:
                empty = (i, row.index(0))
                break
        
        if not empty:
            return self.grid
        
        row, column = empty

        for number in self.possible_values(row, column):
            self.grid[row][column] = number
            solution = self.solve()
            if solution:
                return solution
            else:
                self.grid[row][column] = 0

        return None