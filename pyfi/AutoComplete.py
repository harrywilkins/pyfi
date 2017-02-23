class AutoComplete(): #Author Aidan Horton
    
    def AutoCompleteFast(self, word):
        engDict, i, word = open("Dictionary.txt", "r"), 0, word.lower()
        while currWord != "*":
            currWord, match = engDict.readline().rstrip(), True
            if len(currWord) == len(word):
                for i in range(len(word)):
                    if word[i].isalpha() and word[i] != currWord[i]:
                        match = False
                        break
                if match: return currWord
                        
    def AutoCompleteFull(self, word):
        engDict, currWord, bestWords, word = open("Dictionary.txt", "r"), "", [], word.lower()
        while currWord != "*":
            currWord, match = engDict.readline().rstrip(), True
            if len(currWord) == len(word):
                for i in range(len(word)):
                    if word[i].isalpha() and word[i] != currWord[i]:
                        match = False
                        break
                if match: bestWords.append(currWord)
        return bestWords

    def SpellCheck(self, word):
        engDict, currWord, bestScore, word = open("Dictionary.txt", "r"), "", ["", 0], word.lower()
        while currWord != "*":
            currWord, match = engDict.readline().rstrip(), True
            if len(currWord) == len(word):
                score = 0
                for i in range(len(word)):
                    if word[i] == currWord[i]: score += 1
                if score > bestScore[1]: bestScore = [currWord, score]
        return bestScore[0]
