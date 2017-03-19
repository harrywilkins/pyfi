#Only to be used with ordered number lists
def BinarySearch(numList, item): #Author Aidan Horton
    try:
        if numList[len(numList) // 2] > item:                                                       #If the item in the middle of the list is greater than the item we're looking for
            return BinarySearch(numList[:len(numList) // 2], item)                                  #Perform a recursion of the 'cut' list which expands until it finds the item
        elif numList[len(numList) // 2] < item:                                                     #If the item in the middle of the lsit is less than the item we're looking for
            return BinarySearch(numList[len(numList) // 2 + 1:], item) + len(numList) // 2 + 1      #Perform a recursion of the 'cut' list which expands until it finds the item
        else: return len(numList) // 2                                                              #If there is a match, return the index of the item
    except: False                                                                                   #Any overflow errors will return false

def LinearSearch(itemList, item): #Author Aidan Horton
    for i in range(len(itemList)):          #Iterate through given list
        if itemList[i] == item: return i    #If there is a match, return the index
