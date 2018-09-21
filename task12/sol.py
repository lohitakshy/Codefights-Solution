def commonCharacterCount(s1, s2):
    count = 0
    dict1 ={}
    dict2= {}
    #commons = set(s1) & set(s2)
    #print(commons)
    for i in range(len(s1)):
        dict1[s1[i]] = dict1.get(s1[i],0)+1
        
    for i in range(len(s2)):
        dict2[s2[i]] = dict2.get(s2[i],0)+1
    count = 0
    print(dict1)
    print(dict2)
    for keys,value in dict1.items():
        print(keys,value)
        if keys in dict2.keys():
            count += min(dict2[keys],value)
    return count
    
    ------------------------------------------------------------------------------------------
    
    def commonCharacterCount(s1, s2):
    count = 0
    intersection = set(s1) & set(s2)
    for i in intersection:
        count+= min(s1.count(i),s2.count(i))
    return count
