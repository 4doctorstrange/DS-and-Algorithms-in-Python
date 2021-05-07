arr = list(map(int,input().split()))
k=int(input())
i=0
j=0
ans=[]
lis=[]

while j<len(arr):
    while len(lis)>0 and lis[-1]<arr[j]:   #removing all the elements if commming elementis greater than other
        lis.pop()
    lis.append(arr[j])
    if j-i+1<k:   
        j+=1
    elif j-i+1==k:
        ans.append(lis[0])
        if arr[i] in lis:  #if starting is on list, then we have to remove it as window will slide
            lis.pop(0)
            
        i+=1
        j+=1
       
print(ans)
