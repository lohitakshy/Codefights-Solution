def isLucky(n):
    sum1 = 0
    sum2 = 0
    s1 = str(n)
    x = int(len(s1)/2)
    print(x)
    p = x
    for i in range(x):
        sum1+= int(s1[i])
        sum2+= int(s1[p])
        p+=1
        
    if sum1 == sum2:
        return True 
    else: 
        return False
