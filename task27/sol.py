class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        sum1 = 0
        big_array = []
        index = []
        len1 = 0
        if len(A)==0:
            return []
        else:
            
            for i in range(len(A)):
                if A[i] >= 0 and len(A)-1 != i:
                    index.append(A[i])
                else:
                    if i == len(A)-1 and A[i]>0:
                        index.append(A[i])
                    big_array.append(index)
                    index = []
            sum_check = list(map(sum, big_array))
        #compare = func1(sum_check)
            max_sum = max(sum_check)
            compare = []
            count = 0
            for i,k in enumerate(sum_check):
                if max_sum == k:
                    count+=1
                    compare.append(i)
        #print(big_array)
        #print(compare)
            if len(compare) == 1:
                return big_array[compare[0]]
            else:
                x = len(compare)
                i = 0
                newlist = []
                while x > 0:
                    newlist.append([len(big_array[compare[i]]),compare[i]])
                    i+=1
                    x -= 1
                compare1 = [row[0] for row in newlist]
                #print(compare1)
                max_sum = max(compare1)
                compare = []
                count = 0
                for i,k in enumerate(compare1):
                        if max_sum == k:
                            count+=1
                            compare.append(i)
                if len(compare) == 1:
                    return big_array[newlist[compare[0]][1]]
                else:
                    minindex = min([row[1] for row in newlist])
                    return big_array[minindex]
        
        
