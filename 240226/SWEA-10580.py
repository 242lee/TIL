
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    inputList = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0 
    for t in range(N):
        target = inputList[t]
        for i in range(t, N):
            # print(inputList[i])
            if target[0] < inputList[i][0] and target[1] > inputList[i][1]:
                cnt += 1
            elif target[0] > inputList[i][0] and target[1] < inputList[i][1]:
                cnt += 1
    print(f'#{tc} {cnt}')


# ================================================================
    
def get_result():
    N = len(arr)
    cnt = 0
    for i in range(N):
        for t in range(i):
            i_a, i_b = (arr[i][0], arr[i][1])
            t_a, t_b = (arr[t][0], arr[t][1])
            if i_b < t_b:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        a, b = map(int, input().split())
        arr.append((a,b)) # 튜플
    # 정렬
    arr.sort(key = lambda x : x[0]) #첫번째 원소를 기준으로 오름차순 정렬
    result = get_result()
    print(result)