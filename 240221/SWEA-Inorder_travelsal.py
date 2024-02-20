def inorder(T):
    if T:
        inorder(left[T])
        result.append(inputList[T-1][1])
        inorder(right[T])

for testcase in range(1, 11):
    N = int(input())
    inputList = [list(input().split()) for _ in range(N)]
    # print(inputList)

    parent = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    result = []

    for i in range(N):
        if len(inputList[i]) >= 3:
            left[int(inputList[i][0])] = int(inputList[i][2])
            parent[int(inputList[i][2])] = int(inputList[i][0])
        if len(inputList[i]) >= 4:
            right[int(inputList[i][0])] = int(inputList[i][3])
            parent[int(inputList[i][3])] = int(inputList[i][0])

    inorder(1)
    print(f'#{testcase}',''.join(result))

    '''
    8
    1 W 2 3
    2 F 4 5
    3 R 6 7
    4 O 8
    5 T
    6 A
    7 E
    8 S
    -------------------------------
    print(parent)   [0, 0, 1, 1, 2, 2, 3, 3, 4]
    print(left)     [0, 2, 4, 6, 8, 0, 0, 0, 0]
    print(right)    [0, 3, 5, 7, 0, 0, 0, 0, 0]
    '''