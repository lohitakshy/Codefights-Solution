def prefixSums(a):
    sum1 = 0
    answer = []
    for i in a:
        sum1 += i
        answer += [sum1]
    return answer
