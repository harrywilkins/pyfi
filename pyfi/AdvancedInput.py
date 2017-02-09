class AdvancedInput():
    def sinput(_prompt=">>> "):
        #Author Harry Wilkins
        #Input any value, returns converted value
        
        raw_flags = [0,0,0,0]
        inp = input(_prompt)

        for c in inp:
            raw_flags[0] += 1 if c.isalpha() else 0 #Character is chr
            raw_flags[1] += 1 if c.isdigit() else 0 #Character is int
            raw_flags[2] += 1 if (c in '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~') else 0 #Character is punctuation aside from '.'
            raw_flags[3] += 1 if c == "." else 0 #Character is '.'
            
        flags = [(1 if raw_flags[raw_flags.index(x)] >= 1 else 0) for x in raw_flags] #Normalise flags
        return int(inp) if flags == [0,1,0,0] else (float(inp) if flags == [0,1,0,1] else str(inp)) #Compare and convert


    def InputFormat(inpFormat, separateWords=True, prompt=">>> "):
    #Author Aidan Horton
    while True:
        inp, match = input(prompt), True
        _inp = inp.split() if separateWords else inp
        if len(_inp) != len(inpFormat): continue
        for i in range(len(inpFormat)):
            if not SmartInput.DataType(_inp[i], inpFormat[i]): match = False
        if match: return inp

    #Sees if 'inp' is the specified 'dataType' - dataType has types - "int", "float", "alpha", "lower", "upper", "str", "space"
    def DataType(inp, dataType):
        #Author Aidan Horton
        if dataType == "int" or dataType == "float":
            try: return {"int":isinstance(eval(inp), int), "float":isinstance(eval(inp), float)}[dataType]
            except: return False
        return {"lower":inp.islower(), "alpha":inp.isalpha(), "upper":inp.isupper(), "space":inp.isspace(), "str":True}[dataType]






























""" Class A Write Off
class Table():

    def __init__(self, rows=0, columns=0, spacing=0):
        self.rows = rows
        self.columns = columns
        self.widths = {}
        self.spacing = spacing
        
        self.GenerateBoard()

    def GenerateBoard(self):
        self.table = [[0 for x in range(self.rows)] for x in range(self.columns)]
        self.UpdateBoard()
        
    def SetCell(self, _pos, _value):
        if self.table != None:
            if _pos[0] <= self.columns - 1 and _pos[1] <= self.rows - 1:
                self.table[_pos[0]][_pos[1]] = _value
            else:
                Debug.Log(2, "Table/SetCell({0},{1},{2}):_pos is out of table bounds".format(self,_pos,_value))
        self.UpdateBoard()
    def UpdateBoard(self):
        self.widths = {}
        for column in self.table:
            self.widths[tuple(column)] = max([len(str(x)) for x in column])

        self.maxRowLength = 0
        for x in range(self.rows):
            r = 0
            for column in range(self.columns):
                r += len(str(self.table[column][x])) + self.spacing
            if r > self.maxRowLength:
                self.maxRowLength = r + self.rows
            
            
                 
        
        

    def DisplayBoard(self):
        print("-"*self.maxRowLength)
        for y in range(self.columns):
            row = ""
            for x in range(self.rows):
                row += str(self.table[x][y])
                row += (" " * self.spacing) + (" " * ((self.widths[tuple(self.table[x])]) - len(str(self.table[x][y])))) + "|"
            print("|" + row)
        print("-"*self.maxRowLength)
        
t = Table(8,8, 4)
t.SetCell([1,2], "Meme")
t.UpdateBoard()"""

