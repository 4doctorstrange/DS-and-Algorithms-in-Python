#FLIP THE STRING    -> NOVEMBER COOK_OFF
for _ in range(int(input())):
    a=input()
    b=input()
    ans=0
    i=0
    n=len(a)
    while(i<n):   #checking odd indexes which need inversion,step=2 as only odd indexd can be inberted in one go
        if a[i]!=b[i]:
            while i<len(a) and a[i]!=b[i]:  #agr koi bit beech me same aati hai to "i" whi tk run hoga, aur  waha tk ki substring ko invert krenge aur ans+=1 hoga
                i+=2
            ans=ans+1               # us for loop wale i se jo bhi index invert kr skte the, wo ho gye aur ek count ans ka increase ho gya
        i+=2
    
    i=1
    while(i<n):  # checking even indexes now of "a" string
        if a[i]!=b[i]:
            while i<len(a) and a[i]!=b[i]:
                i+=2
                
            ans=ans+1
        i+=2
    print(ans)
        