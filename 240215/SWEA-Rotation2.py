T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(M):
        arr.append(arr.pop(0))
    print(f'#{testcase} {arr[0]}')

'''
T = int(input())
 
for tc in range(T):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
 
    for _ in range(m):
        number.append(number.pop(0))
 
    print(f'#{tc+1} {number[0]}')
    
'''