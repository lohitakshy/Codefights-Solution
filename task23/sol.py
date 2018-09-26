def addBorder(picture):
    result = []
    x = len(picture[0])+2
    z = (x - len(picture[0]))//2
    for i in range(len(picture)):
        if i == 0:
            result.append(x * '*')
        p = z*'*' + picture[i] + z*'*'
        result.append(p)
    result.append(x*'*')        
    return result
