T = int(input())
for tc in range(1, T+1):
    sdoku = [list(map(int, input().split()))for _ in range(9)]
    result = [True, True, True]

    # 1. 가로 줄 판별
    cnt1 = 0
    for i in range(9):
        if len(set(sdoku[i])) == 9:
            cnt1 += 1
    if cnt1 != 9:
        result[0] = False

    # 2. 세로 줄 판별
    cnt2 = 0
    for j in range(9):
        mini1 = []
        for i in range(9):
            mini1.append(sdoku[i][j])
        if len(set(mini1)) == 9:
            cnt2 += 1
    if cnt2 != 9:
        result[1] = False

    # 3. 3 * 3 판별
    cnt3 = 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            mini2 = []
            for p in range(3):
                for q in range(3):
                    if 0 <= i + p < 9 and 0 <= j + q < 9:
                        mini2.append(sdoku[i+p][j+q])
            if len(set(mini2)) == 9:
                cnt3 += 1
    if cnt3 != 9:
        result[2] = False

    if sum(result) == 3:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
