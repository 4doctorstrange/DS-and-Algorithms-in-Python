def hanoi(s,d,h,n):
    if n==1:
        print("moving plate",n,"from",s,"to",d)
        return
    hanoi(s,h,d,n-1)     #moving plates from source to helper using destination
    print("moving plate",n,'from',s,"to",d)
    hanoi(h,d,s,n-1)
    
    
n=5  #take any number of discs
hanoi('source','destination','helper',n)