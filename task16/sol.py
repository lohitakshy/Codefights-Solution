def caseUnification(inputString):
        
        lower_count = sum(map(str.islower, inputString))
        upper_count = sum(map(str.isupper, inputString))
        if lower_count >= upper_count:
                result = inputString.lower()
        else:
            result = inputString.upper()
        return result


---------------------------
count in different manner

for l in inputString:
        if 'A' <= l <= 'Z':
            up += 1
        else:
            down += 1
