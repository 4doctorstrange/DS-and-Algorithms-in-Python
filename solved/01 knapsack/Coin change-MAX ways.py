#COIN CHANGE PROBLEM- MAx NUMBER OF Ways
# unbounded 0/1
#*Almost same as subset sum
def subset_sum():
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                cache[i][j]=0
            if j==0:
                cache[i][j]=1
                
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                cache[i][j]= cache[i][j-arr[i-1]] + cache[i-1][j]  #only change is that if the choice is selected, then we leave a scope to take action on this item in future.
            else:
                cache[i][j]=cache[i-1][j]
    
    
    
arr=[1,2,3]
s=5
n=len(arr)
cache=[[-1 for i in range(s+1)] for j in range(n+1)]
subset_sum()
print(cache[n][s])
