def willYou(young, beautiful, loved):
    if young and beautiful and not loved:
        #print('this')
        return True
    elif loved == True and (young == False or beautiful == False):
        #print('this1')
        return True
    else:
        return False
        
