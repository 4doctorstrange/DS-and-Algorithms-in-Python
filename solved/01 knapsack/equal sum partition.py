#IN TOP-DOWN BASE CONDITION OF RECCURSSION BECOMES INITIALIZATION OF MATRIX AND CHOICE DIAGRAM BECOMES THE MATRIX SUBPROBLEMS

def equalsum():
    # Initialization will be same as SUBSET SUM 
    ##Initializing first row and first column (here first column will be true always as it is always possible to make subset that have sum=0 , except cache[0][0] all elements of first row will be False as it is not possible to generate a particular sum with 0 elements. SO initialization will take place accordingly:
    for i in range(n+1): 
        for j in range(s+1):   
            if i==0:
                cache[i][j]=False
            if j==0:
                cache[i][j]=True
    #FILLING MATRIX:
    for i in range(1,n+1):  # this loop selects element from array
        for j in range(1,s+1):
            if arr[i-1]<=j:
                cache[i][j]=cache[i-1][j-arr[i-1]] or cache[i-1][j]
            else:
                cache[i][j]=cache[i-1][j]
                
arr=[1,3,7,9]
s=sum(arr)
if s%2==1:
    print("SUm not possible")
else:
    s=s//2
    n=len(arr)
    cache=[[-1 for i in range(s+1)]for j in range(n+1)]
    equalsum()
    print(cache[n][s])
