def splitByValue(k, elements):
    result = []
    for i in range(len(elements)):
        if elements[i] < k:
            result.append(elements[i])
    #result.append(k)
    for i in range(len(elements)):
        if elements[i] >= k :
            result.append(elements[i])
            
    return result
            
   

