T = int(input())
for tc in range(1, T+1):
    N = int(input())
    point = []
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if (x ** 2) + (y ** 2) <= (N ** 2):
                point.append((x, y))
    print(f'#{tc} {len(point)}')
