#CODE to find number of those subsets with given differnece 
# Also a solution for taget sum i.e dividing array  in two parts such tht the differnece os thir sum == target

def count_subset_differnence():
    #initialiing is same as subset sum
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                cache[i][j]=0
            if j==0:
                cache[i][j]=1
                
    #filling is also same as previous questions
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                cache[i][j]=cache[i-1][j-arr[i-1]] + cache[i-1][j]
            else:   
                cache[i][j]=cache[i-1][j]
   
                
arr=[1,1,2,3]
diff=1
count=0
n=len(arr)
s=(diff+sum(arr))//2
cache=[[-1 for i in range(s+1)]for j in range(n+1)]

count_subset_differnence()
print(cache[n][s])

# proof to get 's':
# s1-s2=diff
# s1+s2=sum
# s1=(diff-sum)/2
# SO ultimately we need to find those subsets whose sum is s1:
# hence that will be value of s