'''
Problem Description:

Given a string s, find the length of the longest substring without repeating characters.

'''
s = input()
k=0
i=0
j=0
ans=0
dic=[]
while j<len(s):
    dic.append(s[j])
    if len(set(dic))==len(dic):
        ans=max(ans,j-i+1)
        j+=1
    else: 
        while len(set(dic))!=len(dic):
            dic.pop(0)
            i+=1
        j+=1
       
print(ans)
