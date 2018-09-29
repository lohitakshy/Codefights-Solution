def reverseParentheses(s):
    i = 0
    count = s.count('(')
    if count ==0:
        result=s
    while count > 0:
        if s[i] == "(":
            open1 = i
        if s[i] == ")":
            close1 = i
            count-=1
            result = s[:open1]+s[open1+1:close1][::-1]+s[close1+1:]
            i = 0
            s = result
            print(result)
        i+=1
    #print(result)
    return result
    
    
    -------------------------------------
    
    Other solution --> 
    
    def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s
