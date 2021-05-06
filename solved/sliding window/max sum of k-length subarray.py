arr = [100,200,300,400]
n= 4
k = 2 #size of window or sub array
i=0
j=0
mx=-1
s=0
while j<n:
    s = s+arr[j]
    if j-i+1<k:   #if j is not at windo's end
        j+=1
    elif j-i+1==k:
        mx = max(mx,s)
        s -=arr[i]   #removing i'th block of beginning
        i+=1
        j+=1
print(mx)
    