class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = {}

    def setCell(self, cell: str, value: int) -> None:
        c, r = ord(cell[0]) - 65, int(cell[1:]) - 1
        self.grid[(r, c)] = value

    def resetCell(self, cell: str) -> None:
        c, r = ord(cell[0]) - 65, int(cell[1:]) - 1
        self.grid.pop((r, c), None)

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        return self.val(x) + self.val(y)

    def val(self, s: str) -> int:
        if s[0].isalpha():
            c, r = ord(s[0]) - 65, int(s[1:]) - 1
            return self.grid.get((r, c), 0)
        return int(s)
