class MathSeq(): #Author Harry Wilkins
    def Fibonacci(_iterations=1, _range=-1):
        _seq = [0,1,1]
        for x in range(_iterations):
            _seq.append(_seq[x+2] + _seq[x+1])
        print(_seq[:-3])
