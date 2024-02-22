di = [0,1,1,1,0,-1,-1,-1]
dj = [1,1,0,-1,-1,-1,0,1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    heightInfo = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            # 주변 높이 모음 리스트
            check = []
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    check.append(heightInfo[ni][nj])
            # print(check)
            # 착륙지랑 check 리스트랑 비교해서 착륙지보다 높이 낮은 지역 수 구하기
            cnt = 0
            for height in check:
                if height < heightInfo[i][j]:
                    cnt += 1
            # 그 수가 4 이상일 때만 후보지에 포함
            if cnt >= 4:
                result += 1
    print(f'#{tc} {result}')