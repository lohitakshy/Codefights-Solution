def fibonacciIndex(n):
    length = n
    if length == 1:
        return 0
    f1 = 0
    f2 = 1
    n2 = str(f1+f2)
    index1 = 1
    while len(n2) != length:
        f3 = f1+f2
        f1 = f2
        f2 = f3
        n2 = str(f3)
        index1+=1
    return index1    
    
