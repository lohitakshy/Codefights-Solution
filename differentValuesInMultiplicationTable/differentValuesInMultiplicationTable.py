def differentValuesInMultiplicationTable(n, m):
    list1 = []
    for i in range(n):
        for j in range(m):
            list1.append((i+1)*(j+1))
    return len(set(list1))
