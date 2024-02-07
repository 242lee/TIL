T = int(input())
for testcase in range(1, T+1):
    ps = input().rstrip()   

    L = list()
    for p in ps:
        if p == '(' or p == ')' or p == '[' or p == ']':
            if len(L) == 0:
                L.append(p)
            else:
                if p == "(" or p == '[':
                    L.append(p)
                else:
                    if p == ')':
                        if L[-1] == "(":
                            L.pop()
                        else:
                            L.append(p)
                    
                    if p == ']':
                        if L[-1] == "[":
                            L.pop()
                        else:
                            L.append(p)      

    if len(L) == 0:
        print("yes")
    else:
        print("no")