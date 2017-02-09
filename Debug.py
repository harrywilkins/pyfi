class Debug():
    #Author Harry Wilkins
    supression = [0,0,0]
    log = {0:[],1:[],2:[]}

    #LogType #Message
    #0       #Log
    #1       #Warning
    #2       #Error
    
    def Log(_logType, _value):
        Debug.log[_logType].append({0:"Log: ",1:"Warning: ",2:"Error: "}[_logType] + str(_value))
        if Debug.supression[_logType] == 0: print(Debug.log[_logType][-1])
        
    def PrintLog():
        for key in list(Debug.log.keys()):
            [print(x) for x in Debug.log[key]]

















