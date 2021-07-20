#First and Last occurence of a number
#Count of particular elemnent will be (lc-fc +1)
def binary_search(arr,n,k):
    s=0
    e=n-1
    
    fc= -1
    lc = -1
    while s<=e:
        mid = (s+e)//2
        if arr[mid]==k:
            #fc = mid
            #e=mid-1
            lc=mid
            s=mid+1
            
        elif k>arr[mid]:
            s=mid+1
        elif k<arr[mid]:
            e=mid-1
            
    #return fc
    return lc

arr= [1,3,4,5,5,5,5,9,10,23]
n=len(arr)
k=5
print(binary_search(arr,n,k))      














