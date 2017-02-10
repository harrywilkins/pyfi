class Searching(): #Author Aidan Horton

    #Only to be used with ordered number lists
    def BinarySearch(self, numList, item):
        try:
            if numList[len(numList) // 2] > item:
                return self.BinarySearch(numList[:len(numList) // 2], item) 
            elif numList[len(numList) // 2] < item:
                return self.BinarySearch(numList[len(numList) // 2 + 1:], item) + len(numList) // 2 + 1
            else: return len(numList) // 2
        except: False

    def LinearSearch(self, itemList, item):
        for i in range(len(itemList)):
            if itemList[i] == item: return i
