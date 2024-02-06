'''
N, M = map(int, input().split())
wordlist = [input() for _ in range(N)]
#가로
for i in range(N):
    for j in range(M):
        if wordlist[i][j:-1] == wordlist[i][M-j+1:0:-1]:
            print(wordlist[i])
'''
N, M = map(int, input().split())
wordlist = [input() for _ in range(N)]
#세로
for i in range(N):
    newList = []
    for j in range(M):
        for k in range(N):
            print(newList.append(wordlist[k][j]))