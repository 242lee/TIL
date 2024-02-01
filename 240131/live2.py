# bit = [0,0,0,0]

# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)
#-------------------------------------
# N = 3
# arr = [1,2,3]

# for i in range(1<<N):
#     s= 0
#     for j in range(N):
#         if i&(1<<j):  # j번째 값이 1이면
#             s+= arr[j]
#             print(arr[j], end = ' ')
#     print(f', sum = {s}')

'''
     -> 공집합
1 
2
1 2
3
1 3
2 3
1 2 3
'''
#-------------------------------------
def f(arr, N):
    for i in range(1, 1<<N):
        s= 0
        for j in range(N):
            if i&(1<<j):  # j번째 값이 1이면
                s+= arr[j]
            # print(arr[j], end = ' ')
    # print(f', sum = {s}')
            if s == 0:
                return True
        return False

N = int(input())
arr = list(map(int, input().split()))

print(f(arr,N))