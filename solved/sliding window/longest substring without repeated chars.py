
'''
Problem Description:

Given a string s, find the length of the longest substring without repeating characters.

'''
#Only differnce is that size of dictionary must be equal to size of window
s = input()
k=0
i=0
j=0
ans=0
dic={}
while j<len(s):
    dic[s[j]] = dic.get(s[j],0) + 1
    if len(dic)>j-i+1:       
        j+=1
    elif len(dic)==(j-i+1):    
        ans = max(ans,j-i+1)
        j+=1
    elif len(dic)<(j-i+1): 
        while len(dic)<(j-i+1):
            dic[s[i]]-=1
            if dic[s[i]]==0:
                dic.pop(s[i])
            i+=1
        j+=1
       
print(ans)
