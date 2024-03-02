T = int(input())
for tc in range(1, T+1):
    ground = list(input())
    now = ''
    cnt = 0
    for each in ground:
        if each == '(':
            cnt += 1
        if each == ')'and now == '|':
            cnt += 1
        now = each
    print(f'#{tc} {cnt}')