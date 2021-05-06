#Kth smallest integer
import heapq    #by default it will give min heap so we will multiply each element by -1
arr=list(map(int,input().split()))
k=3
hp=[]
i=0
n=len(arr)
while i<n:
    print(hp)
    heapq.heappush(hp,-1*(arr[i]))   #adding elements
    if len(hp)>k:
        heapq.heappop(hp) 
    i+=1
print(heapq.heappop(hp)*-1)  #returns the Kth smallest element