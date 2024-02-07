N, M = map(int, input().split())
inputBoard =[input() for _ in range(N)]

# 8 * 8 배열 체스판은 두 가지 종류
CB1 = [
    'WBWBWBWB', 
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
       ]
CB2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
       ]

min_cnt = 50*50
#입력된 체스판에서 v부터 v+8까지 탐색하기
for i in range(N - (8 - 1)):
    for j in range(M - (8 - 1)):
        #체스보드 1번과 비교했을 때 최솟값 찾기
        cnt = 0
        for k in range(8):
            if inputBoard[i + k][j:j + 8] != CB1[k]:
                for l in range(8):
                    if inputBoard[i + k][j + l] != CB1[k][l]:
                        cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt
        #체스보드 2번과 비교했을 때 최솟값 찾기
        cnt = 0
        for k in range(8):
            if inputBoard[i + k][j:j + 8] != CB2[k]:
                for l in range(8):
                    if inputBoard[i + k][j + l] != CB2[k][l]:
                        cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt

print(min_cnt)