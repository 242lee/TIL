N = int(input())
numList = list(map(int, input().split()))
# 당근 총 개수
sumnum = sum(numList)

L = -1
R = N

Leftsum = 0
Rightsum = 0

while L < R:
    if Leftsum < Rightsum:
        L += 1
        if L < R:
            Leftsum += numList[L]
        else:
            L -= 1
            break
    
    else:
        R -= 1
        if L < R:
            Rightsum += numList[R]
        else:
            R += 1
            break
    result  = abs(Leftsum - Rightsum)
    