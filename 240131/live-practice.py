# 5x5 대각선

N = 5

# for c in range(N):
#     for r in range(N):
#         print(f'({c}, {r})', end = ' ')
#     print()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
n =5

total = 0
for i in range(N):
    total += arr[i][i]  # 오른쪽 아래 대각선
    total += arr[i][N-1-i]
if N%2: # 크기가 홀수인 경우
    total -= arr[N//2][N//2]    # 중심원소가 중복되므로
print(total)