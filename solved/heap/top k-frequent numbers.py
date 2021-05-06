'''
PROBLEM: TOP-K FREQUENT NUMBER.
STATEMENT: Given an array, we have to output 'k' numbers with most frequency
APROACH: we will use MIN-HEAP and in heap we will input tuple having 2 integers, one            will be element and other will be that number's freq and sorting/placing in heap
       will be based on frequencies. We will maintain k size of heap and pop all those          tuple with less freq so that at the end we have numbers with more freqs
'''
import heapq
arr=list(map(int,input().split()))
dic={}
k=2
n=len((arr))
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
hp=[]
for i in dic:
    tup=(dic[i],i)
    heapq.heappush(hp,tup)
    if len(hp)>k:
        heapq.heappop(hp)
        
while hp:  #poppinng the remaining element
    p=heapq.heappop(hp)
    print(p[1])
    
        
    
    