'''
PROBLEM: An arrray and an integer(x) is given. we have to give k-closest elements to the integer

Approach: We will use max-heap and populate it with a tuple having 2 integers. first will be absolute difference of the integer x and array elements and 2nd will 
	be the array element(NOTE: in case of tuple as heap element, arrarngement will be based on first element of tuple i.e abs diff AND 
	basically we want those elements whose abs diff is minimum , SO we are popping  that tuple whose first index does not qualify for our answer)
'''
import heapq
x=int(input())
arr=list(map(int,input().split()))
n=len(arr)
k=3
i=0 
hp=[]
while i<n:
    heapq.heappush(hp,(abs(arr[i]-x)*(-1),arr[i]))
    if len(hp)>k:
        heapq.heappop(hp)
    i+=1
for i in hp:
    print(i[1],end=" ")
    
    
    