T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    cnt = 0

    for case in range(N):
        zone = list(map(int, input().split()))
        for zone_i in range(zone[0], zone[2]+1):
            for zone_j in range(zone[1], zone[3]+1):
                if arr[zone_i][zone_j] == (3-zone[4]):
                    arr[zone_i][zone_j] = 3
                else:
                    arr[zone_i][zone_j] = zone[4]

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{testcase} {cnt}')
    
        # zone1 = list(map(int, input().split()))
        # zone2 = list(map(int, input().split()))

        # #zone1 색칠되는 구역
        # for z1_i in range(zone1[0], zone1[2]+1):
        #     for z1_j in range(zone1[1], zone1[3]+1):
        #         if arr[z1_i][z1_j] == 2:
        #             arr[z1_i][z1_j] = 3
        #         else:
        #             arr[z1_i][z1_j] = 1

        # #zone2 색칠되는 구역
        # for z2_i in range(zone2[0], zone2[2]+1):
        #     for z2_j in range(zone2[1], zone2[3]+1):
        #         if arr[z2_i][z2_j] == 1:
        #             arr[z2_i][z2_j] = 3
        #         else:
        #             arr[z2_i][z2_j] = 2

        # for i in range(10):
        #     for j in range(10):
        #         if arr[i][j] == 3:
        #             cnt += 1

        # print(f'#{testcase} {cnt}')