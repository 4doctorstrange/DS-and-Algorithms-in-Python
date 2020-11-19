def lcs(x,y,m,n):
    max_length=0     #max_length
    ending_index=m    #stores ending of lcs in x
    cache=[ [0 for i in range(n+1)] for j in range(m+1) ]  #making martix
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                cache[i][j]=cache[i-1][j-1]+1
                
                if cache[i][j]>max_length:  #checking with max_lenght of current cell
                    max_length=cache[i][j]
                    ending_index=i
                    
    return x[ending_index-max_length:ending_index]
                    

x=input()
y=input()
m=len(x)
n=len(y)
print("longest commom substring is:",lcs(x,y,m,n))
