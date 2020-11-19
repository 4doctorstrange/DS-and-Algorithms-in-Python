def lcs(x,y,m,n,count):
    if m==0 or n==0:
        return count   # getting answer
    if x[m-1]==y[n-1]:
        count= lcs(x,y,m-1,n-1,count+1)   #incrementing count if equality is found
        
    count=max(count,lcs(x,y,m-1,n,0),lcs(x,y,m,n-1,0))  # initializing count with maximum of count and other to possible anwers
    return count
    
x=input()
y=input()
m=len(x)
n=len(y)
cache=[ [0 for i in range(n+1)] for j in range(m+1) ]
print("length of longest commom substring is:",lcs(x,y,m,n,0))
