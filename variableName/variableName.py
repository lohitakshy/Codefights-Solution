def variableName(name):
    if name[0].isdigit():
        return False
    for i in name:
        if i.isalpha() or i.isdigit() or i =='_':
            pass
        else:
            return False
    return True

------------------------------
# Compare like this 
 if (not ('a' <= name[i] and name[i] <= 'z' or
                    'A' <= name[i] and name[i] <= 'Z' or
                    '0' <= name[i] and name[i] <= '9' or
                    name[i] == '_')):
