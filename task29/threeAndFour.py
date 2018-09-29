def threeAndFour(n):
    result = []
    if n < 12:
        return [0]
    for i in range(n):
        if i%3 == 0 and i%4 == 0:
            result.append(i)
    return result
