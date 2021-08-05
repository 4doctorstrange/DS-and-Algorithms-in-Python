#for this we calculate index of minimum number which will divide the array in two sorted 
#arrays and then apply normal binary search

def binary_search(s,n,k):
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==k:
            return mid
        if k>arr[mid]:
            s=mid+1
        if k<arr[mid]:
            e=mid-1
    return -1

def get_minimum(s,n,k):
    e=n-1
    while s<=e:
        mid=(s+e)//2
        upper= (mid+1)%n
        lower = (mid+n-1)%n
        if arr[mid]<arr[upper] and arr[mid]<arr[lower]:
            return mid
        elif arr[s]<=arr[mid]: #array is sorted
            s=mid+1
        elif arr[e]>=arr[mid]: #array is sorted so, min will be in unsorted
            e=mid-1
        
            
        
arr=[3,4,5,1,2]
n=len(arr)
k=2
minimum = get_minimum(0,n,k)
print("minimum index is:",minimum)
first_sorted=binary_search(0,minimum,k)
second_sorted=binary_search(minimum,n,k)
print("element is at: ",max(first_sorted,second_sorted) )