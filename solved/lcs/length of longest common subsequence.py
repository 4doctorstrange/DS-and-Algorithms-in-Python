def lcs(a,b,m,n,cache):
    if m==0 or n==0:
        return 0
    len_strs=(m,n)

    if (m,n) not in cache:
        if a[m-1]==b[n-1]:
            cache[(m,n)]= lcs(a,b,m-1,n-1,cache)+1
        else:
            cache[(m,n)]=max(lcs(a,b,m-1,n,cache),lcs(a,b,m,n-1,cache))

    return cache[(m,n)]


a=input()
cache={}
b=input()
print("Length of common subsequence is:",lcs(a,b,len(a),len(b),cache))