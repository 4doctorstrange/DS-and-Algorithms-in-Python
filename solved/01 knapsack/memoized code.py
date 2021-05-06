def ks(weight,value,w,n):
    if n==0 or w==0:
        return 0
    
    if cache[n][w]!=-1:
        return cache[n][w]
    
    if weight[n-1]<=w:
        cache[n][w]=max(value[n-1]+ ks(weight,value,w-weight[n-1],n-1),ks(weight,value,w,n-1))
    else:
        cache[n][w]=ks(weight,value,w,n-1)
    return cache[n][w]
    
weight=[10,20,30]
value=[60,100,120]
w=50
n=len(value)
cache=[[-1 for j in range(w+1)]for i in range(n+1)]   #making matrix
print(ks(weight,value,w,len(value)))
