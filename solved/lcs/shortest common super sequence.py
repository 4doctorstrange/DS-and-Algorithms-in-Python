#ADITYA VERMA WALI APPROACH BHI USE KR SKTE HAIN JISME PEHLE DONO STRING KA LCS NIKAL LO
# AUR m+n-LCS WILL BE ANSWER ....



#DYNAMIC CACHE IS SAME AS LCS AS , so that is not included here.
def scs(x,y,m,n):
    if m==0 or n==0:    
        return m+n  # TO return the  remaining legth of other string(jiski length zero nhi hui hai , uski length as it is return hogi,::-->>OBVIOUSLY)
    if x[m-1]==y[n-1]:
        return scs(x,y,m-1,n-1)+1
    
    return min(scs(x,y,m-1,n)+1,scs(x,y,m,n-1)+1)    
    
x=input()
y=input()
print("length of shortest common super sequence is:",scs(x,y,len(x),len(y)))