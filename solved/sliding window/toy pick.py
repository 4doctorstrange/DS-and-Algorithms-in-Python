'''
Problem Description:

John is at a toy store help him pick maximum number of toys. He can only select in a continuous manner and he can select only two types of toys.
'''
#Only differnce is that size of dictionary must be equal to size of window
s = input()
k=2
i=0
j=0
ans=0
dic={}
lis={}
while j<len(s):
    dic[s[j]] = dic.get(s[j],0) + 1
    if len(dic)<2:       #if there are less than 2 types of toys-> add toys
        j+=1
    elif len(dic)==2:      #if types of toys==2->
        ans = max(ans,j-i+1)   #current window size will give an answer
        j+=1
    elif len(dic)>2:           #if size_dict >2, start removing from front
        while len(dic)>2:
            dic[s[i]]-=1
            if dic[s[i]]==0:
                dic.pop(s[i])
            i+=1
        j+=1
       
print(ans)
