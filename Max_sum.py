#Maximum sum of subarray of size 4
#TC : O(N**2) 
# constant variable
def Max_Sum(arr,k):
    n = len(arr)
    Max = 0
    for i in range(0,n):
        for j in range(i,n):
            if len(arr[i:j+1]) == k:
                Max = max(Max,sum(arr[i:j+1]))
    return Max
    
print(Max_Sum([1,3,10,7,4],3))
