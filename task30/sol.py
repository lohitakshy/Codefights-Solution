def knapsackLight2(weight1, weight2, maxW):
    if weight1+weight2 <= maxW:
        return 'both'
    elif weight1 <= maxW and weight2 <= maxW:
        return 'either'
    elif weight1 <= maxW and weight2 > maxW:
        return 'first'
    elif weight1 > maxW and weight2 <= maxW : 
        return 'second'
    else: return 'none'

    

