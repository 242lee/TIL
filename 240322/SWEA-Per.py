'''
N개의 수열에서 합이 K가 되는 것
'''
def find(lst, i):
    global cnt 
    if sum(result) == K:
        cnt += 1
        return
    for i in range(i,N):
        result.append(nums[i])
        find(lst + [nums[i]], i + 1)
        result.pop()

T = int(input())
for tc in range(1, T+1):  
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    result = []
    cnt = 0
    find([],0)
    print(f'#{tc} {cnt}')