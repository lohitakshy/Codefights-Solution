def launchSequenceChecker(systemNames, stepNumbers):
    dict1 = {}
    for i in range(len(systemNames)):
        if systemNames[i] not in dict1:
            dict1[systemNames[i]] = stepNumbers[i]
        else:
            if dict1[systemNames[i]] < stepNumbers[i]:
                dict1[systemNames[i]] = stepNumbers[i]
            else: 
                return False
    return True
