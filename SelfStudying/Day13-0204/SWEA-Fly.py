Arr = [[1,2,1,2,3],[3,4,3,4,5],[5,6,5,6,7],[7,8,7,8,9]]
N = 4
M = 5
K = 2 #파리채 크기
maxsum = 0

for i in range(N-(K-1)):
    for j in range(M-(K-1)):
        death = 0
        
        for r in range(K):
            for c in range(K):
                death += Arr[i+r][j+c]

        if maxsum < death:
            maxsum = death

print(death)