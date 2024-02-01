T = int(input())

for testcase in range(1, T+1):

    N = int(input())
    numList = list(map(int, input().split()))

    def selectionsort(numList, N):
        for i in range(N):
            minindex = i
            for j in range(i+1, N):
                if numList[minindex] > numList[j]:
                    minindex = j
            numList[i], numList[minindex] = numList[minindex], numList[i]

    selectionsort(numList, N)
    print(f'#{testcase}', *numList)
    print()
