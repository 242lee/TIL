# 순열 만들기

def f(i,N):
    global min_v
    if i == N:
        # print(*P)
        subsetsum = 0 # 선택한 원소의 합
        for j in range(N):
            subsetsum += arr[j][P[j]] # j 행에서 p[j]열을 고른 경우의 합 구하기
        if min_v > subsetsum:
            min_v = subsetsum
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i] # 자리를 바꾸자
            f(i+1, N)
            P[i], P[j] = P[j], P[i] # 원래대로 돌려놓자

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 100
    f(0, N)
    print(f'{testcase} {min_v}')