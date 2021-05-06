def bubblesort(n):
    j=0
    if n==0:
        return
    
    while j<n-1:
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]  #swap
        j+=1
    bubblesort(n-1)
        
    
arr=[9,6,2,12,11,9,3,7]
bubblesort(len(arr))
print(arr)