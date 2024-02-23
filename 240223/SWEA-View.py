
for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    view = 0
    for h in range(2, N-2):
        # 왼쪽 + 오른쪽
        ad = buildings[h-2:h] + buildings[h+1:h+3]
        if buildings[h] - max(ad) > 0:
            view += (buildings[h] - max(ad))
    print(f'#{tc} {view}')
'''
14
0 0 3 5 2 4 9 0 6 4 0 6 0 0
'''