def Boong():
    sold = 0
    for b in buyer:
        insale = (b//M) * K
        sold += 1
        remain = insale - sold

        if remain < 0:
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    # N명에게 판매, M초의 시간 동안 K 개 붕어빵
    N, M, K= map(int,input().split())
    buyer = list(map(int, input().split()))
    buyer.sort()
    result = Boong()
    print(f'#{tc} {result}')
