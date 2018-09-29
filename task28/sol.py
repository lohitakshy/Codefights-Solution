def arrayChange(inputArray):
    count = 0
    diff =0
    for i in range(len(inputArray)-1):
        if inputArray[i] <= inputArray[i+1]:
            pass
        else:
            diff = abs(inputArray[i+1] - inputArray[i]) + 1
            count+=diff
            inputArray[i+1] = diff+inputArray[i+1]
    return count
