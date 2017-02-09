class Table():
    #Author Aidan Horton
    def __init__(self, x, y, defaultCell=0):
        self.x = x
        self.y = y
        self.defCell = defaultCell
        self.GenerateBoard()

    def GenerateBoard(self):
        self.table = [[self.defCell for x1 in range(self.x)] for y1 in range(self.y)]

    def DisplayBoard(self, spaces=0):
        for yPos in range(self.y):
            for xPos in range(self.x): print(str(self.table[yPos][xPos]) + " " * (spaces - len(str(self.table[yPos][xPos]))) + "\n" * int((xPos + 1) / self.x), end='')

    def GetCell(self, x, y):
        return self.table[y][x]

    def ModifyCell(self, x, y, newVal):
        self.table[y][x] = newVal    

    def GetCellByNumber(self, num):
        return self.table[num // self.y][num - (num // self.x) * self.x]

    def ModifyCellByNumber(self, num, newVal=0):
        self.table[num // self.y][num - (num // self.x) * self.x] = newVal

