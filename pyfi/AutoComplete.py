class AutoComplete(): #Author Aidan Horton
    
    def AutoCompleteFast(self, word):
        engDict, i, word = open("Dictionary.txt", "r"), 0, word.lower()
        while i != "*":
            currWord, match = engDict.readline().rstrip(), True
            if len(currWord) == len(word):
                for i in range(len(word)):
                    if word[i].isalpha() and word[i] != currWord[i]:
                        match = False
                        break
                if match: return currWord
                        
    def AutoCompleteFull(self, word):
        engDict, i, bestWords, word = open("Dictionary.txt", "r"), 0, [], word.lower()
        while i != "*":
            currWord, match = engDict.readline().rstrip(), True
            if len(currWord) == len(word):
                for i in range(len(word)):
                    if word[i].isalpha() and word[i] != currWord[i]:
                        match = False
                        break
                if match: bestWords.append(currWord)
        return bestWords
