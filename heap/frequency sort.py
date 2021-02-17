'''
PROBLEM: Frequency sort.
STATEMENT: Given an array, we have to output array elemnts according to their frequency, i.e numbers with most occurences are placed first
APROACH: we will use MAX-HEAP and look previous example method
'''
import heapq
arr=list(map(int,input().split()))
dic={}
n=len((arr))
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
hp=[]
for i in dic:
    
    tup=(dic[i]*-1,i)
    heapq.heappush(hp,tup)      
while hp:  #poppinng the remaining element
    p=heapq.heappop(hp)
    print(str(p[1])*(-1*p[0]),end=" ")
    
        
    
    
