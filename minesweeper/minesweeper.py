def minesweeper(matrix):
    result = []
    count = 0
    resul1 = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #print(i,j,result,resul1)
            if j+1 <= len(matrix[0])-1:
                if matrix[i][j+1] == True:
                    #print("check j+1 pass")
                    count+=1
            if i+1 <= len(matrix)-1:
                if matrix[i+1][j] == True:
                    #print("check i+1 pass")
                    count+=1
            if j+1 <= len(matrix[0])-1 and i+1 <= len(matrix)-1:
                if matrix[i+1][j+1] == True:
                    #print("check i+1 and j+1 pass")
                    count+=1
            if j-1 >= 0:
                if matrix[i][j-1] == True:
                    #print("check j -1")
                    count+=1
            if i+1 <= len(matrix)-1 and j-1 >= 0:
                if matrix[i+1][j-1] == True:
                    #print("check i+1 j-1")
                    count+=1
            if j+1 <= len(matrix[0])-1 and i-1 >= 0:
                if matrix[i-1][j+1] == True:
                    #print("check j+1 i-1")
                    count+=1
            if i-1 >=0:
                if matrix[i-1][j] ==True:
                    #print("check i-1 j")
                    count+=1
            if i-1 >=0 and j-1>=0:
                if matrix[i-1][j-1]== True:
                    #print("check i-1 j-1")
                    count+=1
            result.append(count)
            count = 0
        resul1.append(result)
        result = []
    return resul1

            
