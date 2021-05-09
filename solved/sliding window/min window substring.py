from collections import Counter
s1 = input()
s2 = input()
k=2
i=0
j=0
ans=9999999
dic=Counter(s2)
size=len(dic)
lis=[]
pika={}
while j<len(s1):
    if s1[j] in dic:
        dic[s1[j]]-=1
        if dic[s1[j]]==0:       #reducing size if occurence of an element is achieved i.e we no longer need to look for it
            size-=1
    if size>0:   # simply incrementing if size is not zero i.e we need elements for substring
        j+=1
    if size==0:     #when size is zero, we get an answer
        ans = min(ans,j-i+1)
        pika[ans] = s1[i:j+1]   #storing strings which can be our answer
        j+=1  
        while size==0 or s1[i] not in dic :         #decresing window size
            if s1[i] in dic:
                dic[s1[i]]+=1
                if dic[s1[i]]==1:
                    size+=1
            i+=1  
            if i>=len(s1):    #for boundary conditions
                break
        j+=1
print(pika[ans])  #this will give final string as once we have traversed the entire string, current value of ans will denotes the smallest window size 
