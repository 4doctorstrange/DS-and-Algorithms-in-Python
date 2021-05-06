#IN THIS NORMAL MATRIX IS TAKEN FOR CACHING INSTEAD OF DICTIONARY.
#ONLY VARIATION IS THAT IF TWO ELEMENTS ARE SAME THEN THEIR INDICES SHOULD NOT BE SAME


def rcs(a,b,m,n):
    if m==0 or n==0:
        return 0
    if cache[m][n]==-1:
        if a[m-1]==b[n-1] and m!=n:
            cache[m][n]=rcs(a,b,m-1,n-1)+1
        else:
            cache[m][n]=max(rcs(a,b,m,n-1),rcs(a,b,m-1,n))
            
    return cache[m][n]


a=input()
m=len(a)
cache=[[-1 for i in range(m+1)] for j in range(m+1)]  
print("longest repeating common subsequence is: ", rcs(a,a,m,m)  )