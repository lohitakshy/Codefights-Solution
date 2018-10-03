def rotateImage(a):
    return numpy.rot90(a,k=3)
-------------------------------------------------
# other solution
def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
