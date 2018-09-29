def isMonotonous(sequence):
    if len(sequence) == 1:
        return True
    else:
        increase = sequence[0] <= sequence[1]
        decrease = sequence[1] <= sequence[0]
        for i in range(len(sequence) - 1):
            print(sequence[i],sequence[i+1])
            if sequence[i] >= sequence[i+1] and increase:
                return False
            elif sequence[i] <= sequence[i+1] and decrease:
                return False
    return True
