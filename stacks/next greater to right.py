
def ngr(arr,n):
    ans=[]
    stack=[]
    #element with zero index is considered at top of stack
    i=n-1
    while i>=0:  # traversing from last
        if len(stack)==0:
            ans.append(-1)
            
        elif len(stack)>0 and stack[0]>arr[i]:    #top>element
            ans.append(stack[0])
            
        elif len(stack)>0 and stack[0]<=arr[i]:
            while len(stack)>0 and stack[0]<=arr[i]:#in loop  until stack become empty or get top>element
                stack.pop(0)
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[0])
                
        stack.insert(0,arr[i])   #inserting at 0th index i.e at top
        i-=1  
            
    print(*ans[::-1])

arr=list(map(int,input().split()))
n=len(arr)
ngr(arr,n)
