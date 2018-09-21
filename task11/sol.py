def allLongestStrings(inputArray):
    max1 = 0
    for i in inputArray:
        if max1 < len(i):
            max1 = len(i)
    ans=[]
    for i in inputArray:
        if len(i) == max1:
            ans.append(i)
    return ans
