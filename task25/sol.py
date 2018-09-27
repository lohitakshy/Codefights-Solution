def lineEncoding(s):
    count = 1
    temp = s[0]
    result = ''
    s = s+" "
    for i in range(1,len(s)):
        print(temp,s[i],count,result)
        if temp == s[i]:
            count +=1
        else:
            if count == 1:
                result+=s[i-1]
            else:
                result += str(count)+str(s[i-1])
            #print(result)
            temp = s[i]
            count = 1    
    return result    
