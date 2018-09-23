def truncateString(s):
    #print(len(s))
    flag = True
    p = s
    while len(p) > 0 and flag == True:
        print(p)
        if int(p[0])%3 == 0:
            p = p[1:]
            i+=1
            print(p)
        elif int(p[-1])%3 == 0:
            p = p[:-1]
            print(p)
        elif (int(p[0])+int(p[-1]))%3 == 0:
            p = p[1:-1]
            print(p)
        else:
            flag = False
    return p
