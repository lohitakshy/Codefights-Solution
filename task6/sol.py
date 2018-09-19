def arrayConversion(inputArray):
    result = inputArray
    result1 = []
    j = 2
    while len(result) > 1:
        print(" result value ")
        print(j)
        print(result)
        result1 = []
        if j%2 == 0:
            for i in range(0,len(result) - 1,2):
                    result1.append(result[i]+result[i+1]) 
                    print(result1)
            result = result1
            j = j + 1
        else:
            for i in range(0,len(result) - 1,2):
                result1.append(result[i]*result[i+1])
                print(result1)
            result = result1
            j = j + 1
            
    return result[0]      
