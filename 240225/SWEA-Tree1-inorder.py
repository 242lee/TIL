'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''
def inorder(T):
    if T:
        inorder(c1[T])
        inorder(c2[T])
        result.append(info[T-1][1])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(str, input().split())) for _ in range(N)]
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    parent = [0] * (N+1)
    result = []
    for i in range(N):
        if len(info[i]) == 3:
            c1[int(info[i][0])] = int(info[i][2])
        if len(info[i]) == 4:
            c1[int(info[i][0])] = int(info[i][2])
            c2[int(info[i][0])] = int(info[i][3])
    inorder(1)
    print(f'#{tc}',''.join(result))