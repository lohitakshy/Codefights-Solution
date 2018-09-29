def removeDuplicateCharacters(str):
    dict1 = {}
    result = ""
    for i in set(str):
            dict1[i] = str.count(i)
    
    for i in str:
        if dict1[i] > 1: continue
        result+=i
    print(dict1)
            
    return result
