class AutoComplete(): #Author Aidan Horton
    
    def AutoCompleteFast(self, word):
        engDict, i = open("Dictionary.txt", "r"), 0
        while i != "*":
            currWord, match = engDict.readline().rstrip(), True
            if len(currWord) == len(word):
                for i in range(len(word)):
                    if word[i] != "_" and word[i] != currWord[i]:
                        match = False
                        break
                if match: return currWords
                        
    def AutoCompleteFull(self, word):
        engDict, i, bestWords = open("Dictionary.txt", "r"), 0, []
        while i != "*":
            currWord, match = engDict.readline().rstrip(), True
            if len(currWord) == len(word):
                for i in range(len(word)):
                    if word[i] != "_" and word[i] != currWord[i]:
                        match = False
                        break
                if match: bestWords.append(currWord)
        return bestWords
