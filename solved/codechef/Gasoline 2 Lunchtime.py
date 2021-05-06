for _ in range(int(input())):
    n=int(input())
    fuel=list(map(int,input().split()))
    cost=list(map(int,input().split()))
    
    sorted_indicesC=[i[0] for i in sorted(enumerate(cost),key=lambda x:x[1])] #this line  will sort indices of array on the basis of values and those indices are stored in array
    ans=0
    distleft=n
    for i in sorted_indicesC:
        temp=min( fuel[i], distleft)  # fuel[i] will basically give fuels of cars in ascending order of cost.
        distleft-=temp
        ans+= temp*cost[i]  #extracting cost of that car
        if distleft==0:
            break
    print(ans)
        