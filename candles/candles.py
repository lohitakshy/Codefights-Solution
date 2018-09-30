def candles(candlesNumber, makeNew):
    leftover = newcandle = candlesNumber
    sum1 = candlesNumber
    while newcandle > 0:
        newcandle = leftover//makeNew
        sum1 +=newcandle
        leftover = leftover%makeNew
        leftover += newcandle
        print(newcandle,sum1,leftover)
    return sum1    
