"""3484. Design Spreadsheet"""

from string import ascii_uppercase


class Spreadsheet:
    def __init__(self, rows: int):
        self.sheet: dict[str, list[int]] = {
            char: [0] * rows for char in ascii_uppercase
        }

    def setCell(self, cell: str, value: int) -> None:
        char = cell[0]
        idx = int(cell[1:]) - 1

        self.sheet[char][idx] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def get_cell(self, cell: str) -> int:
        char = cell[0]
        idx = int(cell[1:]) - 1

        return self.sheet[char][idx]

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split("+")

        left = int(left) if left.isdigit() else self.get_cell(left)
        right = int(right) if right.isdigit() else self.get_cell(right)

        return left + right


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
