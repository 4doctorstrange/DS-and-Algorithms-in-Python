'''
CEILING OF AN ELEMENT IN A SORTED ARRAY:

Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing order. Write efficient functions to find floor and ceiling of x.

'''

def binary_search(arr,n,k):
    s=0
    e=n-1
    res=-1
    while s<=e:
        mid = (s+e)//2
        if k==arr[mid]:
            return arr[mid]
        if k>arr[mid]:
            s=mid+1
        if k<arr[mid]:
            res=arr[mid]
            e = mid-1
    return res
    
arr = list(map(int,input().split()))
k=18
print(binary_search(arr,len(arr),k))