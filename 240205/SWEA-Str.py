T = int(input())
for testcase in range(1, T+1):    
    str1 = input()
    str2 = input()

    cntmax = 0
    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2:
                cnt += 1
        if cntmax < cnt:
            cntmax = cnt  
    print(f'#{testcase} {cntmax}')


