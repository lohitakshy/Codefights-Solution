def divNumber(k, l, r):
    count = 1
    result = 0
    for i in range(l,r+1):
        for j in range(l,r+1):
            #print(i,j)
            if i%j == 0:
                count+=1
        if count==3:
            result+=1
        count = 1
    return result
