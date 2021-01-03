def get_ans(exp):
    stack=[]
    for i in exp:
        if i.isdigit()==True:
            stack.append(i)
        else:
            try:
                a=int(stack.pop())
                b=int(stack.pop())
                if i=="+":
                    ans=a+b
                elif i=="-":
                    ans=b-a
                elif i=="*":
                    ans=a*b
                elif i=="/":
                    ans=b/a
                elif i=="^":
                    ans=b**a
                stack.append(ans)
            except KeyError:
                print('Smething is wrong in exp')
        
    return stack.pop()
exp=input()
print(get_ans(exp))

