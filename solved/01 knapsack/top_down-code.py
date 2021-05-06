#IN TOP-DOWN BASE CONDITION OF RECCURSSION BECOMES INITIALIZATION OF MATRIX AND CHOICE DIAGRAM BECOMES THE MATRIX SUBPROBLEMS

def topdown(weight,value,w):
    ##Initializing first row and first column
    for i in range(n+1): 
        for j in range(w+1):   
            if i==0 or j==0:
                cache[i][j]=0
                
    #FILLING MATRIX:
    for i in range(1,n+1):
        for j in range(1,w+1):
            if weight[i-1]<=j:
                cache[i][j]=max(value[i-1] +cache[i-1][j-weight[i-1]],cache[i-1][j])
            else:
                cache[i][j]=cache[i-1][j]
                
weight=[10,20,30]
value=[60,100,120]
w=50
n=len(value)
cache=[[-1 for i in range(w+1)]for j in range(n+1)]
topdown(weight,value,w)
print(cache[n][w])
