class Variable():
    variables = {}
    
    def __init__(self, _symbol='x', _coe='1', _exp='1', _sign='+'):
        self.symbol = _symbol
        self.coe = _coe
        self.exp = _exp
        self.sign = _sign
class Value():
    
    def __init__(self, _value=0, _sign='+'):
        self.value = _value
        self.sign = _sign
    
#Form of ax + b = const
#Use 2x + 4 = 8
#Find variables
f = input(">>> ")
for c in f:
    if c.isalpha() and c != "e":
        #Found a variable
        currentIndex = list(f).index(c) - 1
        print("Detected variable " + c)
        coe = ""
        #Look back until sign is found, finding sign and coefficient
        while currentIndex >= 0 and list(f)[currentIndex] not in ['+','-']:
            coe += list(f)[currentIndex]
            currentIndex -= 1
        coe = int(coe[::-1])
        print("Detected coefficient " + str(coe))
        sign = "+"
        if currentIndex >= 0:
            sign = list(f)[currentIndex]
        print("Detected sign " + sign)
        #Look forward until a sign is found, finding exponent
