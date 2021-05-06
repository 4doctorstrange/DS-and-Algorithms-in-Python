#PROBLEM: a k-sorted or nearly sorted array is given i.e elements of array are placed correctly upto length k in both leftward and rightward direction. We have to sort array

#Approach: we are populating a min heap by elements of array whose max length can be k, if legth is gr8er than k element is popped and that element will be in its place
import heapq
arr=list(map(int,input().split()))
n=len(arr)
k=4
hp=[]
ans=[]
i=0
while i<n:
    heapq.heappush(hp,arr[i])
    if len(hp)>k:
        ans.append(heapq.heappop(hp))
    i+=1
    
while hp:      #emptying remaining elements of heap
    ans.append(heapq.heappop(hp))
print(ans)
