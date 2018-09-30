def arrayMaximalAdjacentDifference(inputArray):
   return max( abs(inputArray[i] - inputArray[i+1])for i in range(len(inputArray)-1))
