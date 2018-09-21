def makeArrayConsecutive2(statues):
    sat = sorted(statues)
    count = 0
    for i in range(len(sat)-1):
        #print(sat[i],sat[i+1])
        count = count + sat[i+1]-sat[i]-1
    return count

-------------------------
efficient solution --> 

max(statues) - min(statues) - len(statues) + 1
