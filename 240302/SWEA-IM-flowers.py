'''
5 1
'''
T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    water = N // ((D*2)+1)
    if N % ((D*2)+1) != 0:
        water += 1
    print(f'#{tc} {water}')
