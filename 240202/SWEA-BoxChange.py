T = int(input())

for testcase in range(1, T+1):  
    N, Q = map(int, input().split())

    Box = [0] * N
    for i in range(Q):
        L,R = map(int, input().split())
        for j in range(L-1, R):
            Box[j] = (i+1)
        
    print(f'#{testcase}', *Box)