'''
N, M, K
N명의 사람에게, M초에 K개 붕어빵
2 2 2
3 4
'''
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()
    answer = 'Possible'
    cnt = 0
    for t in customer:
        cnt += 1
        if (t//M) * K < cnt:
            answer = 'Impossible'
            break
    print(f'#{tc} {answer}')