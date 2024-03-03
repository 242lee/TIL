'''
4  
10 20 
30 40
60 50
70 80
'''
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    corr = [0] * 200
    for _ in range(N):
        i, j = map(int, input().split())
        if i > j:
            i, j = j, i
        i, j = (i-1)//2, (j-1)//2
        for k in range(i, j+1):
            corr[k] += 1
    print(f'#{tc} {max(corr)}')



