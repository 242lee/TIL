T = int(input())
for tc in range(1, T+1):
    N = int(input())
    inputList = list(input().split())

    '''
    list1 = inputList[:N//2]
    list2 = inputList[N//2:]
    print(list1)
    print(list2)
    result = []
    for i in range((len(list2))):
        result.append(list1[i])
        result.append(list2[i])
        # 길이가 다를 땐 어떻게 해?
    '''

    a = 0
    b = (N+1) // 2
    print(f'#{tc}', end = ' ')
    for t in range(N):
        if t % 2 == 0:
            print(inputList[a], end = ' ')
            a += 1
        else:
            print(inputList[b], end = ' ')
            b += 1
    print()