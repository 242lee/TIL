# A = [1,2,3,4,5,6,7,8,9,10,11,12]
# N=3, K=6 인 경우 3개의 원소를 가지고 원소의 합이 6인 집합

T = int(input())

for testcase in range(1, T+1):
    N, K = map(int, input().split())

    Arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    ArrList = []

    for i in range(1<<len(Arr)):  #모~~~든 경우의 수를 도는 
        innerlist = []
        for j in range(len(Arr)):
            if i&(1<<j):  #
                innerlist.append(Arr[j])
        ArrList.append(innerlist)    

    cnt = 0
    for each in ArrList:
        if len(each) == N and sum(each) == K:
            cnt += 1
    print(f'#{testcase} {cnt}')

#-----------------------------------------------
    
T = int(input())
arr_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1 << len(arr_a)):
        num_li = []
        for j in range(len(arr_a)):
            if i & (1 << j):
                num_li.append(arr_a[j])
        if len(num_li) == N and sum(num_li) == K:
            result += 1
    print(f'#{tc} {result}')

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