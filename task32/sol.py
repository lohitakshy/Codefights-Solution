def palindromeRearranging(inputString):
    dict1 ={}
    for i in inputString:
        dict1[i] = dict1.get(i,0)+1
    count = 0
    #x = list(dict1.keys())[0]
    for values in dict1.values():
        if values %2 != 0:
            count+=1
    if count > 1:
        return False
    else:
        return True
        
        
        --------------------------------------------
        sort version:
           
           return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1
           
           
