

def ngl(arr,n):
    ans=[]
    stack=[]
    #element with zero index is considered at top of stack
    i=0
    while i<n:  # traversing from start
       
        if len(stack)==0:
            ans.append(-1)
        elif len(stack)>0 and stack[0]>arr[i]:
            ans.append(stack[0])
        elif len(stack)>0 and stack[0]<=arr[i]:
            while len(stack)>0 and stack[0]<=arr[i]:
                stack.pop(0)
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[0])
        stack.insert(0,arr[i])
        i+=1
        
    print(*ans)

arr=list(map(int,input().split()))
n=len(arr)
ngl(arr,n)
