k = int(input())
n = int(input())
arr= list(map(int,input().split()))
i=0
j=0
lis=[]
while j<n:
    if arr[j]<0:
        lis.append(arr[j])  #storing negative numbers    
    if j-i+1<k:   #if j is not at window's end
        j+=1
    elif j-i+1==k:
        if len(lis)>0:
            print(lis[0],end= " ")
        else:
            print(0,end=" ")  #if list is empty         
        if arr[i]<0:
            lis.pop(0)
        i+=1
        j+=1