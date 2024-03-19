'''
중복된 순열 1~3까지 숫자 배열이 있을 때 111,112 ~ 332, 333 까지
'''
arr = [i for i in range(1, 4)]
path = [0] * 3


def dfs(level):
    # 기저 조건
    # 이 문제에서 3개를 뽑았을 때 까지 반복
    if level == 3:
        print(*path)
        return

    # 들어가기 전
    # 다음 재귀 호출
    #   - 다음에 갈 수 있는 곳들은 어디인가 ?
    #   - 이 문제에서는 1, 2, 3 세 가지(arr의 길이만큼) 경우의 수가 존재
    path[level] = 1
    dfs(level+1)

    path[level] = 2
    dfs(level+1)

    path[level] = 3
    dfs(level+1)

    # 갔다와서 할 로직
    '''
    중복 가능
    for i in range(len(arr)):
        path[level] = arr[i]
        dfs(level + 1)
    '''
    '''
    중복 불가
    # for i in range(len(arr)):
    #     #갈 수 있을 때만
    #     if arr[i] not in path:
    #         path[level] = arr[i]
    #         dfs(level + 1)
        #갈 수 없을 때엔 컨티뉴
        if arr[i] not in path:
            continue
        path[level] = arr[i]
        dfs(level + 1)
        path[level] = 0
    '''
dfs(0)