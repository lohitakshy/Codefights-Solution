def matrixElementsSum(matrix):
    print(len(matrix[0]))
    sum1= 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j])
            if matrix[i][j] == 0 and i+1 < len(matrix):
                matrix[i+1][j] = 0
                #print(matrix[i+1][j])
            sum1=sum1 + matrix[i][j]
    return sum1
            
