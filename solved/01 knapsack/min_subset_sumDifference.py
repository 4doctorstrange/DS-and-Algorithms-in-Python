#MINIMUM SUBSET SUM DIFFERENCE
def min_sum_subset_differnence():
    #initialiing is same as subset sum
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                cache[i][j]=False
            if j==0:
                cache[i][j]=True
                
    #filling is also same as previous questions
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                cache[i][j]=cache[i-1][j-arr[i-1]] or cache[i-1][j]
            else:
                cache[i][j]=cache[i-1][j]
   
                
arr=[1,5,6,11]
n=len(arr)
s=sum(arr)
cache=[[-1 for i in range(s+1)]for j in range(n+1)]
min_sum_subset_differnence()

#NOW we will work on  last row of Matrix as it represents all the sum subsets possible with all the elements of array for range(0,sum(arr)).

# here we are selecting only those subset that are less than or equal to sum(arr)//2.These subsets basically represent s1 and other subset(if s1 is true ) WILL BE in range (sum(arr/2),sum(arr)) whose value MUST BE EQUAL To sum(Arr)-s1.
# AND equation of our answer = min(abs(s1-s2))
#                            = min(abs(s1-(sum-s1)))
#                            = min(abs(sum-2s1))
# hence further work is done accordingly

ans=[]
for i in range(0,(s//2)+1):
    if cache[n][i]==True:
        ans.append(i)
 
min_diff=9999999
for i in ans:
    temp=abs(s-2*i)
    if temp<min_diff:
        min_diff=temp
        
print(min_diff)
    
    


