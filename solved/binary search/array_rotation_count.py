# find number of times sorted array is rotated
##position of smallest element will give the number of times in sorted rotated array
'''
type of rotation=>
           if(array is LEFT rotated then no_of_rotations is equal to (length - index_of_min_element)%length)
           
           if(  array is RIGHT rotated then no_of_rotations = index_of _min_element)

'''



def binary_search(arr,n):
    s=0
    e=n-1
    while s<=e:
        mid = (s+e)//2
        nex_t = (mid+1)%n
        prev = (mid+n-1)%n
        if arr[s] <= arr[e]: #array is sorted
            return s

        if arr[mid]<prev and arr[mid]<nex_t:   #only smallest element will be smaller than both next and previous
            return mid
        elif arr[s]<=arr[mid]:    #array is sorted from start to mid is sorted, hence smallest will be in unsorted array i.e from mid to end
            s=mid+1
        elif arr[mid]<= arr[e]: #array is sorted from mid to end, hence smallest will be available in unsorted array i.e from s to mid
            e=mid-1 
            
    #return fc
    return -1

#orig = 1,3,4,5,6,9,10,23
arr= [9,10,23,1,3,4,5,6]
n=len(arr)
min_pos=binary_search(arr,n) #ONCE WE GET MINIMUM INDEX AND ARRAY DIVIDES IN 2 PARTS, WE CAN AAPLY NORMAL BS TO FIND ANY OTHER ELEMENT IF ASKED IN BOTH THE PARTS
#here array is left rotated

no_of_rotation = (n-min_pos)%n
print(no_of_rotation)














