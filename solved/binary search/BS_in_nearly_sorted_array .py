'''
SEARCH IN A NEARLY SORTED ARRAY:

Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array. Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].

For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved to previous position.
'''

def binary_search(arr,n,k):
    st=0
    end=n-1
    while st<=end:
        mid = (st+end)//2
        if k==arr[mid]:  #comparing with mid
            return mid
        elif mid-1>=st and arr[mid-1]==k:    #comparing with mid-1
            return mid-1
        elif mid+1<=end and arr[mid+1]==k:   #comparing with mid+1
            return mid+1
        elif k<arr[mid-1]:    
            end=mid-2
        elif k>arr[mid+1]:
            st=mid+2
            
    return -1
arr=[10,3,40,20,50,80,70]
k=70
print(binary_search(arr,len(arr),k))