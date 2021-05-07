from collections import Counter
s1 = input()
s2 = input()
i=0
j=0
ans=0
dic = Counter(s2)  #getting freq of all elements of second string
size = len(dic)
count = size

while j<len(s1):
    #print("before",s1[j], dic, count)
    if s1[j] in dic:
        dic[s1[j]]-=1
        if dic[s1[j]]==0:
            count-=1 
        
    if j-i+1<len(s2):   
        j+=1
    elif j-i+1==len(s2):
        
        if count==0:          #when window size is reached
            ans+=1
        if s1[i] in dic:     #checking of front-> if it is present in s2, it's count will be incremented and if it's count becomes 1 means earlier it was zero which means count was decresed, hence now we have to increase the count of that element
            dic[s1[i]]+=1
            if dic[s1[i]]==1:   
                count+=1
        #print("aftrer",s1[j], dic, count)
        i+=1
        j+=1
       
print(ans)
