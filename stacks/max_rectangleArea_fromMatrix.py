#here 2d matix in broken in 1d array and passed in mlh function that gives max value

def mlh(arr,n):
    stack=[]
    right=[]  #(value,index)
    #filling right first with NSRs
    i=n-1
    while i>=0:
        if len(stack)==0:
            right.append(n)
        elif len(stack)>0 and stack[0][0]<arr[i]:
            right.append(stack[0][1])
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
    
    
    left=[]
    stack=[]
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
    
    max_his=[]
    for i in range(n):
        max_his.append(arr[i]*(abs(right[i]-left[i])-1))
        
    return max(max_his)

def max_rect(arr,n):
    ans=[]
    temp=arr[0]
    for i in range(n):
        if i==0:
            ans.append(mlh(arr[0],n))
        else:
            for j in range(n):
                if arr[i][j]==1:
                    temp[j]=temp[j]+arr[i][j]
                else:
                    temp[j]=0
            m=mlh(temp,n)
            ans.append(m)
            
    
    print('area of max rectange is:',max(ans))
            

if __name__ == "__main__":
    arr=A = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
    n=len(arr)
    max_rect(arr,n)


                
                
                
                
