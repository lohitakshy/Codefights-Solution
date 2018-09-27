
def checkSameElementExistence(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            return True
    #print()
    return False
