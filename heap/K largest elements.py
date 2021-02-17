#K Largest Elements
import heapq      #min heap is imported
arr=list(map(int,input().split()))
k=3
hp=[]
i=0
n=len(arr)
while i<n:
    heapq.heappush(hp,arr[i])   
    if len(hp)>k:
        heapq.heappop(hp) 
    i+=1
print(*hp)  #returns the K largest element , element that are now left in the heap are k largest 