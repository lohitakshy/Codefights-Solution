def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    Flag = False
    if max(yourLeft, yourRight) == max(friendsLeft , friendsRight) and min(yourLeft, yourRight) ==  min(friendsLeft , friendsRight):
        return True
    
    return Flag
