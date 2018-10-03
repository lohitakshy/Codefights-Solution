def arrayMode(sequence):
    import operator
    dict1 ={}
    for i in sequence:
        dict1[i] = dict1.get(i,0)+1
    
    max1 = list(dict1.values())[0] 
    
    index = list(dict1.keys())[0]
    
    for key, values in dict1.items():
       
        if max1 < values:
            max1 =  values
            index  = key
            
        
    return index
   ------------------------------------------------
   dict1 ={}
    for i in sequence:
        dict1[i] = dict1.get(i,0)+1
   return max(dict1.items(), key=operator.itemgetter(1))[0]
