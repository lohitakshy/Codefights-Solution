def caesarBoxCipherEncoding(inputString):
    matrix=[] #define empty matrix
    k = 0
    sr = int(math.sqrt(len(inputString))) 
    #print(len(inputString))
    for i in range(sr):
        result=[]
        for j in range(sr):
            result.append(inputString[k])
            k = k + 1
        matrix.append(result)
    #print(matrix)
    result = ""
    #print(len(matrix))
    for i in range(len(matrix)):
        for row in matrix:
            result+=row[i] 

    return result
