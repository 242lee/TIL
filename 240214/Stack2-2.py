# 순열 만들기

def f(i,k):
    if i == k:
        print(*P)
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i] #자리를 바꾸자
            f(i+1, k)
            P[i], P[j] = P[j], P[i] #자리를 바꾸기 전으로 다시 

# 잘 섞어서 순열 만들게
N = 3 
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
f(0, N)
print(min_v)