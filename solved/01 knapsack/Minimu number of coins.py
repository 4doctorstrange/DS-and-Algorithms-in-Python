#COIN CHANGE PROBLEM- MIN number of coins
# IN THis initialization is differnet
#*Almost same as subset sum


Max=99999999  # A very big number is selected t
def subset_sum():
    for i in range(n+1):      #in this initialization first row is initialised with infinty or very big number{as we need infinite number of zeros to produce a sum} and first column with 0
        for j in range(s+1):
            if j==0:
                cache[i][j]=0
            if i==0:
                cache[i][j]=Max
                
    for j in range(1,s+1):
        i=1
        if j%arr[0]==0:           #here we are initializaing first row if a multiples of a single coin can produce the given then that cell is filled with that number of coins 
            cache[i][j]=j%arr[0]
        else:
            cache[i][j]=Max
                
                
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                cache[i][j]= min(cache[i][j-arr[i-1]] +1 , cache[i-1][j]) # here one is added as we get the desired outcome so that one coin is added in the solution.
            else:
                cache[i][j]=cache[i-1][j]
    
    
    
arr=[1,2,3]
s=5
n=len(arr)
cache=[[-1 for i in range(s+1)] for j in range(n+1)]
subset_sum()
print(cache[n][s])
