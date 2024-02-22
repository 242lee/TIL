N = int(input())
arr = [[0] * 7 for _ in range(2)]

# for i in range(2):
#     for j in range(7):
#         if i == 0 and j < 5:
#             arr[i][j] = N + j
#         elif i == 1 and 4 < j:
#             arr[i][j] = 0

for i in range(4):
    arr[0][i] = N
    N += 1

for i in range(6,2,-1):
    arr[1][i] = N - 1 
    N -= 1

for row in arr:
    print(row)