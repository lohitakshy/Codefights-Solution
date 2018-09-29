#Given array of integers, check whether each integer, that occurs in it, is contained there the same number of times as any other
#integer from the given array.

#Example

#For inputArray = [1, 2, 2, 1], the output should be
#checkEqualFrequency(inputArray) = true;
#For inputArray = [1, 2, 2, 3, 1, 3, 1, 3], the output should be
#checkEqualFrequency(inputArray) = false.


def checkEqualFrequency(inputArray):
    dict1 = {}
    for i in inputArray:
        dict1[i] = dict1.get(i,0)+1
    temp1 = next(iter(dict1.values()))
    print(temp1)
    for i,j in dict1.items():
        if j != temp1:
            return False
    return True
