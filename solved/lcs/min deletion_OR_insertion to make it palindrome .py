#basic idea is to find lcs between str and rev(string) which would result in longest palindrome and thus minimum number of deletions are required 

def lcs(x,y,m,n,cache):
    if m==0 or n==0:
        return 0
    tup=(m,n)
    if tup not in cache:
        if x[m-1]==y[n-1]:
            cache[tup]=lcs(x,y,m-1,n-1,cache)+1
        else:
            cache[tup]=max(lcs(x,y,m,n-1,cache),lcs(x,y,m-1,n,cache))
    
    return cache[tup]
x=input()
m=len(x)
n=len(x)
cache={}
y=x[::-1]
print('minimum deletion required to convert a string in palindrome:',m-lcs(x,y,m,m,cache))