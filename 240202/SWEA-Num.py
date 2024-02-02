'''
소인수분해하기
2 a개 / 3 b개 / 5 c개 / 7 d개 / 11 e개
'''
T = int(input())
for testcase in range(1, T+1):
    Num = int(input())
    cntList = []
    #2로 계속 나눠
    cnt_a = 0
    while Num % 2 == 0:
        cnt_a += 1
        Num = (Num//2)
    cntList.append(cnt_a)
    #3으로 계속 나눠
    cnt_b = 0
    while Num % 3 == 0:
        cnt_b += 1
        Num = (Num//3)
    cntList.append(cnt_b)
    #5로 계속 나눠
    cnt_c = 0
    while Num % 5 == 0:
        cnt_c += 1
        Num = (Num//5)
    cntList.append(cnt_c)
    #7로 계속 나눠
    cnt_d = 0
    while Num % 7 == 0:
        cnt_d += 1
        Num = (Num//7)
    cntList.append(cnt_d)
    #11로 계속 나눠
    cnt_e = 0
    while Num % 11 == 0:
        cnt_e += 1
        Num = (Num//11)
    cntList.append(cnt_e)

    print(f'#{testcase}', *cntList)

#----------------------------------------
#개천재 ㅋㅋ
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    abcde_li = [2,3,5,7,11]
    div_li = [0]*5
    i = 0
    while N > 1:
        if N % abcde_li[i] == 0:
            N //= abcde_li[i]
            div_li[i] += 1
        else:
            i += 1
    print(f'#{tc}',*div_li)