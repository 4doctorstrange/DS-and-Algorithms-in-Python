def stock_span(arr,n):  #find out consecutively samller or equl elemnent in left to an element 
    #stack top is considered element at 0th index
    
#PARENT-> NEAREST GREATER TO LEFT
    stack=[]  #stack will store ngl as well as index
    ans=[]   # ans will store index of ngl
    i=0
    while i<n:
        if len(stack)==0:
            ans.append(-1)
            
        elif len(stack)>0 and stack[0][0]>arr[i]:  #0th inddx->element, 1th->index
            ans.append(stack[0][1])
            
        elif len(stack)>0 and stack[0][0]<=arr[i]:
            while len(stack)>0 and stack[0][0]<=arr[i]:
                stack.pop(0)          #popping jb tk ngl nhi mil jata
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[0][1])
        stack.insert(0,(arr[i],i))            
        i+=1
    
    
    for i in range(n):
        print(i-ans[i], end=" ")

arr=list(map(int,input().split()))
n=len(arr)
stock_span(arr, n)

