N, M, R, G = map(int, input().split())
'''
0 호수, 1 배양액 뿌릴 수 있는 땅, 2 뿌릴 수 없는 땅
'''
garden = [list(map(int, input().split())) for _ in range(N)]

# 처음에 배양액 뿌릴 수 있는 땅을 저장
save = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 1:
            save.append((i, j))

while save:
    # p, q는 save에서 pop 해 오려고
    p, q = save.pop(0)
    # 각 1번 땅에 주어진 R과 G를 뿌려
    dp = [0,1,0,-1]
    dq = [1,0,-1,0]
    for k in range(4):
        np = p + dp[k]
        nq = q + dq[k]
        # 범위 내에서만 퍼져나가게
        if 0 <= np < N and 0 <= nq < M:
            # 1. 만약에 1번 땅이면
            if garden[np][nq] == 1:
                garden[np][nq] = garden[p][q]
            # 2. 만약 옆에 반대 색이 있으면 꽃으로 바뀌어
                # 2-1) 나 "빨강" 옆 칸 "초록"이면
            elif garden[p][q] == 'R' and garden[np][nq] == 'G':
                garden[np][nq] = 'F' # 꽃이 돼
                # 2-2) 나 "초록" 옆 칸 "빨강"이면
            elif garden[p][q] == 'G' and garden[np][nq] == 'R':
                garden[np][nq] = 'F' # 꽃이 돼
