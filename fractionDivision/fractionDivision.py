def fractionDivision(a, b):
    def gcd(a,b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)
    x =  a[0]*b[1]
    y = a[1]*b[0]
    #print(x)
    gcd1 = gcd(x,y)
    #print(gcd1)
    return [x/gcd1, y/gcd1]
