#printing all lcs:
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
    
    print(set(getlcs(a,b,m,n)))
    
def getlcs(a,b,m,n):
    
    ans=[]
    if m==0 or n==0:
        ans.append("")
        return ans
    
    if a[m-1]==b[n-1]:
        c=a[m-1]     #storing common character
        temp= getlcs(a,b,m-1,n-1)  #temp contain all the lcs
        for i in temp:
            ans.append(i+c)    #adding common character to all lcs
        return ans
            
    else:
        if cache[m-1][n]>cache[m][n-1]: #lcs from bottom to top
            ans=getlcs(a,b,m-1,n)
        
        if cache[m][n-1]>cache[m-1][n]:  #lcs right to left
            ans=getlcs(a,b,m,n-1)
        
        if cache[m-1][n]==cache[m][n-1]:  #lcs from both bottom to up and left to right
            ans=getlcs(a,b,m-1,n) + getlcs(a,b,m,n-1)
            
        return ans
            
    
    
    
a="AGTGATG"
b="GTTAG"
m=len(a)
n=len(b)
cache=[[-1 for i in range(n+1)] for j in range(m+1)] #row=>a, col->b
lcs(a,b,m,n)