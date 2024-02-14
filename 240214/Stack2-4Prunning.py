# 가지치기
def f(i,k,subsetsum):
    global min_v
    if i == k:
        # print(*P)
        # subsetsum = 0 # 선택한 원소의 합
        # for j in range(k):
        #     subsetsum += arr[j][P[j]] # j 행에서 p[j]열을 고른 경우의 합 구하기
        if min_v > subsetsum:
            min_v = subsetsum
    elif subsetsum > min_v:
        return
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i] #자리를 바꾸자
            f(i+1, k, subsetsum+arr[i][P[i]])
            P[i], P[j] = P[j], P[i] #자리를 바꾸기 전으로 다시 

# 잘 섞어서 순열 만들게
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
f(0, N, 0)
print(min_v)