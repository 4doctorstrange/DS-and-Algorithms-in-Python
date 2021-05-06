def LIS(arr,n):
    
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and cache[i]<cache[j]+1:    #lis holds when elemnt at i > element at j and we update cache only when we get grater value for some j
                cache[i]=cache[j] + 1    
                
    return max(cache)

arr = list(map(int,input().split()))
n=len(arr)
cache=[1 for i in range(n)]  #initially LIS = 1 i.e a single element is always an LIS
print(LIS(arr,n))
