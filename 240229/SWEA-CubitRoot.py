
T = int(input())
for tc in range(1, T+1):
    N = int(input())
 
    cubicroot = -1
    a = round(N ** (1/3))
    if a * a * a == N:
        cubicroot = a
 
    print(f'#{tc} {cubicroot}')
