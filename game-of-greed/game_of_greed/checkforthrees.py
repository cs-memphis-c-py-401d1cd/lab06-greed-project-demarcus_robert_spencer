def checkforthrees(listOfElems):
    ''' Check if given list contains any threes '''    
    for elem in listOfElems:
        if listOfElems.count(elem) == 3:
            return elem
    return False