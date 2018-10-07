def variableName(name):
    if name[0].isdigit():
        return False
    for i in name:
        if i.isalpha() or i.isdigit() or i =='_':
            pass
        else:
            return False
    return True
