def binary_search(l,h):
    mid = (l+h)//2
    if l>h:
        return -1
    if arr[mid] ==key :
        return mid
    elif key>arr[mid]:
        l=mid+1
        return binary_search(l,h)
    elif key<arr[mid]:
        h=mid-1
        return binary_search(l,h)
        



arr = list(map(int,input().split()))
n=len(arr)
key=int(input())
print(binary_search(0,n-1))


'''
def binarysearch( arr, n, k):
		s=0
		end = n-1
		while s<=end:
		    mid = (s+end)//2
		    if k==arr[mid]:
		        return mid
		    if k>arr[mid]:
		        s=mid+1
		    if k<arr[mid]:
		        end=mid -1
	
	    return -1
'''
 
#Binary search in Descending sorted array
def binary_search(arr,n,k):
    s=0
    e=n-1
    while s<=e:
        mid = (s+e)//2
        if arr[mid]==k:
            return mid
        elif k>arr[mid]:
            e=mid-1
        elif k<arr[mid]:
            s=mid+1
    return -1

arr= [20,17,16,14,12,10,8,5,2]
n=len(arr)
k=1
print(binary_search(arr,n,k))      














