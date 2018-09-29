def sortByHeight(a):
    p=[]
    for i in a:
        if i >= 1:
            p.append(i)
    p = sorted(p)
    print(p)
    for index1,value in enumerate(a):
        if value == -1:
            p.insert(index1,value)
    return p
        
