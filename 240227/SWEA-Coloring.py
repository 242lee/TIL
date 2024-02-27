'''
2
2 2 4 4 1
3 3 6 6 2
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr[i] - 시작i, 시작j, 끝i, 끝j, 색
    Board = [[0] * 10 for _ in range(10)]

    # 리스트를 돌아가며
    for k in range(N):
        for i in range(arr[k][0], arr[k][2]+1):
            for j in range(arr[k][1], arr[k][3]+1):
                Board[i][j] += arr[k][4]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    totallen = 0
    for i in range(10) :              
        for j in range(10) :
            if Board[i][j] == 1 or Board[i][j] == 2 : 
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        if Board[ni][nj] != Board[i][j]:
                            totallen += 1
                    else:
                        totallen += 1
    print(f'#{tc} {totallen}')

'''     
                for di, dj in ([[0,1], [0,-1], [1,0], [-1,0]]) :
                    if 0<= i+di < 10 and 0<= j+dj < 10 : 
                        if Board[i+di][j+dj] != Board[i][j] : 
                            totallen += 1  
                    else :               
                        totallen += 1
'''