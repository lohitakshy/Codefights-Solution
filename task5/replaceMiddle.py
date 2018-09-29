def replaceMiddle(arr):
    print(len(arr))
    if len(arr)%2 == 0:
        len1 = int(len(arr)/2)
        print(len1)
        p = (arr[len1]+arr[len1 - 1 ])
        arr.pop(int(len(arr)/2))
        arr[int(len(arr)/2)] =  p
    else:
        pass
    return arr
