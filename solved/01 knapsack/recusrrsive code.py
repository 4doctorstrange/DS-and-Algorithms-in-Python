def ks(weight,value,w,n):
    if n==0 or w==0:
        return 0
    elif weight[n-1]<=w:
        return max(value[n-1]+ ks(weight,value,w-weight[n-1],n-1),ks(weight,value,w,n-1))    #getting maximum from :1-item is included and function is called ,2-item is not included and function is called
    else:
        return ks(weight,value,w,n-1)  # item can't be included
    
weight=[10,20,30]
value=[60,100,120]
w=50
print(ks(weight,value,w,len(value)))
