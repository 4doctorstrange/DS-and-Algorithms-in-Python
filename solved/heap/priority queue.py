class maxheap:
    def __init__(self,items=[]):
        self.heap=[0]       #list with zero at begnning to make sure 1-based indexing
        for i in items:
            self.heap.append(i)
            self.float_up(len(self.heap)-1)
            
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
        
    def float_up(self,index):
        parent=index//2 #integer div
        if index<=1:
            return   # we know a single node is already balanced
        
        elif self.heap[index]>self.heap[parent]:
            self.swap(index,parent)
            self.float_up(parent)   #it may be possible that current parent might be greater than his parent
            
    def bubbledown(self,index):
        left = index*2
        right = left+1
        largest = index
        if len(self.heap)>left and self.heap[largest]<self.heap[left]:  #first part ->to ensure left child exist
            largest = left
            
        if len(self.heap)>right and self.heap[largest]<self.heap[right]:  #to ensure right child exist
            largest = right
            
        if largest!=index:
            self.swap(index,largest)
            self.bubbledown(largest)
    
    def printheap(self):
        print(*self.heap)
        
    def push(self,data):
        self.heap.append(data)
        self.float_up(len(self.heap)-1)
        
    def pop(self):
        if len(self.heap)>2:
            self.swap(1,len(self.heap)-1)    #max priority element is swapped with last element
            k=self.heap.pop()   #removing max priority element
            self.bubbledown(1)    # arranging the swapped element into heap 
            
        elif len(self.heap)==2:
            k=self.heap.pop()           #incase of 2 elements we can safely pop it 
        else:
            k= False        #NO element in heap
        return k
    
arr=list(map(int,input().split()))
h = maxheap(arr) 
print("Max heap generated:",end=" ")
h.printheap()
print("Checking push function:",end= ' ')
h.push(100)
h.printheap()
print("checking priority queue: ")
for i in range(len(arr)+1):
    print("highest priority element=",end=" ")
    m=h.pop()
    print(m)
    print("heap with remaining elements=",end=" ")
    h.printheap()
                 
                
                
