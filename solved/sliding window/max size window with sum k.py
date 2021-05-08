'''
Problem Description:

Given an array containing N positive integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.
'''
arr = list(map(int,input().split()))
k=int(input())
i=0
j=0
ans=-1
s=0
while j<len(arr):
    s +=arr[j]
    if s<k:       #if sum is less than k, keep inc window size
        j+=1
    elif s==k:    #if sum==k, append the window size
        ans = max(ans,j-i+1)
        j+=1
    elif s>k:    #if sum>k, start removing element from starting
        while s>k:
            s-=arr[i]
            i+=1
        j+=1
       
print(ans)
