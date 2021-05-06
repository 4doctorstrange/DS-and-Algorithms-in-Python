def solve(arr,k,cur):
    if len(arr)==1:
        print(arr[0])
        return arr
    cur=(cur+k)%len(arr)
    arr.pop(cur)
    solve(arr,k,cur)
    
n=int(input())
arr=[x for x in range(1,n+1)]
k=int(input())
k=k-1
cur=0
solve(arr,k,cur)