def magicalWell(a, b, n):
    sum1 = 0
    for i in range(n):
        sum1 = sum1 + a*b
        a+=1
        b+=1
    return sum1
