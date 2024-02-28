T = int(input())
for tc in range(1, T+1):
    # N 밭 길이, M 한 번에 옮길 수 있는 당근 수
    N, M = map(int, input().split())
    carrot = [0] + list(map(int, input().split()))
    i = 1
    movecnt = 0
    now = 0
    while 0 < sum(carrot):
        # 한 번에 다 옮길 수 없을 때
        if M-now <= carrot[i]:
            carrot[i] -= (M-now)
            now = 0
            movecnt += 2 * i # i 로 갔다가 집으로 가는 거리
        # 한 번에 옮길 수 있는 수보다 당근 수가 적을 때
        elif M-now > carrot[i]:
            now += carrot[i]
            carrot[i] = 0
            i += 1
        elif carrot[i] == 0:
            i += 1
    # 집으로 들어가야 다녀온 거리를 더해주는 조건이기 때문에
    # 지금 집에 못 들어가서 강제로 마지막에 다녀온 거리 더해줘
    movecnt += i * 2
    print(f'#{tc} {movecnt - 2}')
