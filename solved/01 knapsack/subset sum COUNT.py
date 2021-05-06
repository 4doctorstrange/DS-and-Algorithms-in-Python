#IN TOP-DOWN BASE CONDITION OF RECCURSSION BECOMES INITIALIZATION OF MATRIX AND CHOICE DIAGRAM BECOMES THE MATRIX SUBPROBLEMS
#code gives the number of subsets with given sum
def countsubset():
    # Initialization will be 0 or 1 
    for i in range(n+1): 
        for j in range(s+1):   
            if i==0:
                cache[i][j]=0
            if j==0:
                cache[i][j]=1
                
    #FILLING MATRIX:
    for i in range(1,n+1):  # this loop selects element from array,filling matrix in bottom up manner.
        for j in range(1,s+1):
            if arr[i-1]<=j:
                cache[i][j]=cache[i-1][j-arr[i-1]] + cache[i-1][j] #here we will take all the possibilities so we use '+' 
            else:
                cache[i][j]=cache[i-1][j]
                
arr=[2,3,5,8,7,10]
s=15
n=len(arr)
cache=[[-1 for i in range(s+1)]for j in range(n+1)]
countsubset()
print(cache[n][s])
