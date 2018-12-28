def linear(arr, target):
    
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

linear([2,3,4,6,7],4)
        