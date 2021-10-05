inp = int(input())
for i in range(inp):
    user_input = int(input())
    st = input()

    if st.count('H') == st.count('T'):
        flag = 0
        count=0
        for i in st:
            if i == ".":
                count+=1
                if count == user_input:
                    print("Valid")
                continue
            elif i == "H":
                if flag == 0:
                    flag = 1
                    count+=1
                    continue
                else:
                    print("Invalid")
                    break
            elif i == "T":
                if flag == 1:
                    flag = 0
                    count+=1
                    if count == user_input:
                        print("Valid")
                    continue
                else:
                    print("Invalid")
                    break
    elif st.count('.')==user_input:
        print("Valid")
    else:
        print("Invalid")