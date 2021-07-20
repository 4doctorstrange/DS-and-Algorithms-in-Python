'''
FIND FLOOR OF AN ELEMENT IN A SORTED ARRAY:

Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x. Write efficient functions to find floor of x.

'''
def binary_search(arr,n,k):
    s=0
    e=n-1
    res = -1
    while s<=e:
        mid = (s+e)//2
        if k==arr[mid]:
            return mid
        if k<arr[mid]:
            e= mid-1
        if k>arr[mid]:
            res=mid
            s=mid+1
            
    return res
            
arr = [1, 2, 8, 10, 10, 12, 19]
k = 16
print(binary_search(arr,len(arr),k))
