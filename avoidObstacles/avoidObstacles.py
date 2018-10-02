# trick is to check hit at every element by increase number 1 everytime 

def avoidObstacles(inputArray):
    check_hit = 1
    while True:
        if sorted([value%check_hit for value in inputArray])[0]>0:
            return check_hit
        check_hit += 1
            
