def boxBlur(image):
    list1 = []
    result = []
    sum1 = 0
    length_row = len(image[0]) - 3 + 1
    length_columb = len(image) - 3 + 1
    print(length_row,length_columb)
    for k in range(length_columb): 
        for l in range(length_row):
            for i in range(k,k+3):
                for j in range(l,l+3):
                    sum1+=image[i][j]
            list1.append(sum1//9)
            sum1= 0
        result.append(list1)
        list1 =[]
    return result
        
                
            
        
