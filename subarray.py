def subarray(arr,n,t):
    if n == 0:
        return False
    if t == 0:
        return True
    
    if arr[n-1] > t:
        return subarray(arr,n-1,t)
    return  subarray(arr,n-1,t-arr[n-1]) or subarray(arr,n-1,t) 
        
arr = [1,3,6,8]
t = 10
n = len(arr)
print(subarray([1,2,3,1,4],5,7))
