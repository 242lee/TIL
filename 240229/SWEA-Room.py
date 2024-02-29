
N = int(input())
Board = [list(map(int, input().split()))for _ in range(N)]
move = []
for i in range(N):
    sr = Board[i][0]
    er = Board[i][1]
    move.append((sr, er))
move.sort(key= lambda x: x[1])
# print(move)

# Target을 하나 정하고, 범위 밖에 있는 조합을 찾아
# 둘은 동시에 이동해
cnt = 0
e = -1
for sr, er in move:
    if sr > e:
        cnt += 1
    e = er
# print(cnt)
result = N - cnt + 1
print(result)

# ==========================================

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corr = [0] * 400
    maxcnt = 0

    for _ in range(N):
        s, e = map(int(input().split()))

        if s % 2 == 0:
            s -= 1
        if e % 2 == 0:
            e -= 1

        if s > e:
            s, e = e, s

        for i in range(s, e+1):
            corr[i] += 1
            maxcnt = max(corr[i], maxcnt)
    print(f'{tc} {maxcnt}')