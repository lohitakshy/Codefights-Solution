def isIPv4Address(inputString):
    if len(inputString) < 7:
        return False
    else:
        x =  inputString.split('.')
        if len(x) !=4:
            return False
    for i in x:
        if i.isdigit() and len(i) != 0 and 0<= int(i) <=255:
            pass
        else:
            return False
        
    return True
            
            
