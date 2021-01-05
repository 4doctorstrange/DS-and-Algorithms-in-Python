#PARENT -> NSL and NSR of an element fill form a range of the width of rectange for a particular height/element

def max_histogram(arr,n):
    right=[]    #will hold indices of nsr
    stack=[]
    #first finding NSRs
    i=n-1
    while i>=0:
        if len(stack)==0:
            right.append(n)   #n, as we have assumed the value after n-1 is smaller
        elif len(stack)>0 and stack[0][0]<arr[i]:
            right.append(stack[0][1])   #apppending index
            
        elif len(stack)>0 and stack[0][0]>=arr[i]:
            while len(stack)>0 and stack[0][0]>=arr[i]:
                stack.pop(0)
                
            if len(stack)==0:
                right.append(n)
            else:
                right.append(stack[0][1])
        
        stack.insert(0,(arr[i],i))
        i-=1
    
    right=right[::-1]
    print("right=>",right)
    
    stack=[]
    left=[]
    #calculating NSLs
    i=0
    while i<n:
        if len(stack)==0:
            left.append(-1)
            
        elif len(stack)>0 and stack[0][0]<arr[i]:
            left.append(stack[0][1])
            
        elif len(stack)>0 and stack[0][0]>=arr[i]:
            while len(stack)>0 and stack[0][0]>=arr[i]:
                stack.pop(0)
            if len(stack)==0:
                left.append(-1)
            else:
                left.append(stack[0][1])
        stack.insert(0,(arr[i],i))
        i+=1
        
    print("left",left)
    max_rect=[]
    for i in range(n):
        width=abs(left[i]-right[i])-1
        area=width*arr[i]
        max_rect.append(area)
        
    print("max area is:",max(max_rect))
        
            

    
arr=list(map(int,input().split()))
n=len(arr)
max_histogram(arr,n)
    










