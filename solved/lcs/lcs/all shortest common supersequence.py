
def scs(x,y,m,n,cache):
    if m==0:
        return [y[:n]]
    if n==0:
        return [x[:m]]
    
    if x[m-1]==y[n-1]:
        t=x[m-1]
        temp=scs(x,y,m-1,n-1,cache)
        for i in range(len(temp)):
            temp[i]+=t
        return temp
    #when last character is not same , we will check top and left
    
    if cache[m-1][n]>cache[m][n-1]:  #top>left :-> we will go in left direction as it will give answer with shorest scs
        temp=scs(x,y,m,n-1,cache)
        return [i + y[n-1] for i in temp]  #y wala hr aswer me add hoga jo temp me aayga
    
    if cache[m][n-1]>cache[n][m-1]: #left>top :-go in up direction 
        temp=scs(x,y,m-1,n,cache)
        return [i +x[m-1] for i in temp]
    
    left=scs(x,y,m,n-1,cache)
    top=scs(x,y,m-1,n,cache)
    return [i + y[n-1] for i in left]+[j +x[m-1] for j in top]
   
if __name__ == "__main__":
    x=input()
    m=len(x)
    y=input()
    n=len(y)

    cache=[[0 for i in range(n+1)] for j in range(m+1)]  # creating cache
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                cache[i][j]=cache[i-1][j-1]+1
            else:
                cache[i][j]=min(cache[i-1][j]+1,cache[i][j-1]+1)
                
    ans=scs(x,y,m,n,cache)
    print("all supersequences are:",set(ans))
                
                








