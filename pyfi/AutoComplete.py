def AutoCompleteFast(word): #Author Aidan Horton
    engDict, i, word = open("Dictionary.txt", "r"), 0, word.lower()
    while i != "*":
        currWord, match = engDict.readline().rstrip(), True
        if len(currWord) == len(word):
            for i in range(len(word)):
                if word[i].isalpha() and word[i] != currWord[i]:
                    match = False
                    break
            if match: return currWord
                    
def AutoCompleteFull(word): #Author Aidan Horton
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

def SpellCheck(word): #Author Aidan Horton
    engDict, currWord, bestScore, word = open("Dictionary.txt", "r"), "", ["", 0], word.lower()
    while currWord != "*":
        currWord, match = engDict.readline().rstrip(), True
        if len(currWord) == len(word):
            score = 0
            for i in range(len(word)):
                if word[i] == currWord[i]: score += 1
            if score > bestScore[1]: bestScore = [currWord, score]
    return bestScore[0]

def SCInput(prompt=">>> "):
    sentence = []
    for word in input(prompt).split(): sentence.append(SpellCheck(word[:-1] if "," == word[-1] or "." == word[-1] else word))
    return sentence
