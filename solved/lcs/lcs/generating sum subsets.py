ans=[]
def solve(inp,op,tar):
    if sum(op)>tar:
        return
    if len(inp)==0:
        if sum(op)==tar:
            ans.append(op)
            return
        return    
    op1=op[:]
    op2=op[:]
    op2.append(inp[0])
    inp=inp[1:]
    solve(inp,op1,tar)
    solve(inp,op2,tar)
inp=[1,2,3,4,5]
op=[]
tar=4
solve(inp,op,tar)
print(ans)
print(len(ans))

##############################################################
#SECOND APPROACH 
lis=[]
def solve(arr,n,v,k):
    if (k == 0) : 
        lis.append(v)
        return
    
    if (n == 0): 
        return
 
    solve(arr, n - 1, v, k) #last element not included  sum
    v1 = [] + v             #this basically makes a new copy of list(v)
    v1.append(arr[n - 1])   # appending the element
    solve(arr, n - 1, v1, k - arr[n - 1])  #last element included
 

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    k=sum(arr)//2
    solve(arr,n,[],k)
    m=9999999
    
    for i in lis:
        if len(i)<m:
            m=len(i)
    print(m)
    
