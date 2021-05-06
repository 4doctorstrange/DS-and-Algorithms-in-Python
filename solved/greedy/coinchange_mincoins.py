
def coin(v,arr):
    c=0
    ans=[]
    arr.sort(reverse=True)
    for i in arr:
        if i>v:
            continue
        elif i==v:
            c+=1
            ans.append(i)
            break
        else:
            v-=i
            c+=1
            ans.append(i)
    return (ans,c)
        
v=int(input())
arr=[ 1, 2, 5, 10, 20, 50, 100, 500, 1000]
print(coin(v,arr))