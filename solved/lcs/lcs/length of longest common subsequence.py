#length of longest common subsequence
def lcs(a,b,m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                cache[i][j]=0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                cache[i][j]=cache[i-1][j-1]+1
            else:
                cache[i][j]=max(cache[i-1][j],cache[i][j-1])
        
    
    
a=input()
b=input()
m=len(a)
n=len(b)
cache=[[-1 for i in range(n+1)] for j in range(m+1)] #row=>a, col->b
lcs(a,b,m,n)
print(cache[m][n])
