# 부분집합 구하기
arr = ['A', 'B', 'C', 'D', 'E']
N = len(arr)

def count(target):
    cnt = 0
    for i in range(N):
        if target & 0x1:
            cnt += 1
        target >>= 1
    return cnt

result = 0
for target in range(1<<N):
    if count(target) >= 2:
        result += 1
print(result)

# For문으로 조합 구현하기
arr = ['A', 'B', 'C', 'D', 'E']
N = len(arr)

for a in range(N):
    start1 = a + 1
    for b in range(start1, N):
        start2 = b + 1
        for c in range(start2, N):
            print(arr[a], arr[b], arr[c])
#------------------------------------
arr = ['A', 'B', 'C', 'D', 'E']
N = len(arr)
T = 3
result = []
def combi(depth, start):
    if depth == T:
        print(result)
        return
    for i in range(start, N):
        result.append(arr[i])
        combi(depth+1, i+1)
        result.pop()

combi(0, 0)

#======================================
N = 3
result = []

def func(depth, start):
    if depth == N:
        print(result)
        return
    for i in range(start, 7):
        result.append(i)
        func(depth + 1, i)
        result.pop()

# =======================================
# 화장실 문제

timeList = [15, 30, 50, 10]
N = len(timeList)
timeList.sort()
waitingtime = 0
for i in range(N):
    waitingtime += timeList[i] * (N-i-1)
print(waitingtime)

#===========================================

# Fractional
N = 3 #물건 3개
target = 30
things = [(5, 50), (10, 60), (20, 140)]
things.sort(key= lambda x: (x[1]/x[0]), resverse = True)
sum = 0

for kg, price in things:
    per_price = price/kg
    if target < kg:
        sum += target * per_price
        break
    sum += price
    target -= kg
print(int(sum))
#===========================================
# 회의실 배정
'''
설계) 종료시간을 기준으로 오름차순 정렬
시작 시간이 같은 회의가 있다면 끝나는 시간이 빠른 걸 골라
10
1 4  1 6  6 10  5 7  3 8  5 9  3 5  8 11  2 13  12 14
'''
N = int(input()) # 회의 개수
arr = list(map(int, input().split()))
meeting = []
for i in range(N):
    si, ei = arr[i*2], arr[i*2+1]
    meeting.append((si,ei))
# 종료시간 기준으로 오름차순 정렬
meeting.sort(key = lambda x : x[1])
cnt = 0
fi = 0
for i in range(N):
    if meeting[i][0] >= fi:
        cnt += 1
        fi = meeting[i][1]
# ========================================
# N에서 2개를 고르는 조합
N = 5
for i in range(N-1):
    for j in range(i+1, N):
        if arr[i] + arr[j]//

# ==============================================
def ncr(n, r, s):
    if r == 0:
        print(*combi)
    else:
        for i in range(s, n-r+1):
            combi[r-1] = A[i]
            ncr(n,r-1,i+1)
N = 5
A = [1,2,3,4,5]
R = 3 #골라야 하는 수
combi = [0] * R
ncr(N,R,0)