#lenght of longest common substring

def lcs():
    for i in range(m+1):    #initialization
        for j in range(n+1):
            if i==0 or j==0:
                cache[i][j]=0
            
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                cache[i][j]=cache[i-1][j-1]+1
            else:
                cache[i][j]=0
    ma=-1
    for i in range(m+1):        #returning max as string can exist any where
        for j in range(n+1):
            if cache[i][j]>ma:
                ma=cache[i][j]
    print(ma)
    return ma
      
    
x=input()
y=input()
m=len(x)
n=len(y)
cache=[[-1 for i in range(n+1)] for j in range(m+1) ]
print("length of longest commom substring is: ",lcs())
