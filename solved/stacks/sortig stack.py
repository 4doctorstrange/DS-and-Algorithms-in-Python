  
#SORTS IN DESCENDING ORDER

def insert(s,elm):
    if len(s)==0 or elm<=s[-1]:     #if elm is smaller than top , then append and retunr => base condition
        s.append(elm)
        return
    else:
        temp = s.pop()  #if top> elm, pop it and again use insert to get correct position of elm
        insert(s, elm)  
        s.append(temp)  # now add the removed element
        

def sorted(s):   # basically remove a number all the number recurssively and then start sorting 
    # Code here 
    if len(s)!=0:   
        temp=s.pop()  
        sorted(s)
        insert(s,temp)   # inserting temp in its place in s
        return s

s=list(map(int,input().split()))
print(sorted(s))