'''
PROBLEM : Given of array denoting length of ropes, output minimum cost of combining all the ropes, the cost of combining any 2 ropes is sum of their length
APPROACH:  we will use min-heap, basic idea is that we will pop two ropes with min length, add them, sum will stored and pushed back in heap and continue the process, once the length of heap is 1(which should be sum(arr)) we will break out of loop and add all the result
'''

import heapq

arr=list(map(int,input().split()))
n=len(arr)
s=0
heapq.heapify(arr)           #quicky creating min-heap using built in function
while True:
    if len(arr)==1:
        print("checking last element(should be sum(arr)):",arr[0])
        break
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    t = a+b
    s+=t
    heapq.heappush(arr, t)
    
print("minimum cost:",s)

