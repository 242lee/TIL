
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

print(f'{cnt}')