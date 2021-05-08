'''
Problem Description:

Given a string you need to print the size of the longest possible substring that has exactly k unique characters.

'''
s = input()
k=int(input())
i=0
j=0
ans=-1
dic={}
while j<len(s):
    dic[s[j]] = dic.get(s[j],0) + 1
    if len(dic)<k:       
        j+=1
    elif len(dic)==k:    
        ans = max(ans,j-i+1)
        j+=1
    elif len(dic)>k: 
        while len(dic)>k:
            dic[s[i]]-=1
            if dic[s[i]]==0:
                dic.pop(s[i])
            i+=1
        j+=1
       
print(ans)
