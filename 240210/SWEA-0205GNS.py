T = int(input())
for testcase in range(1, T+1):
    N = input().split()
    numDict = {}
    numList = "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
    for num in numList:
        numDict[num] = 0

    caseList = input().split()
    for case in caseList:
        for keys in numDict.keys():
            if case == keys:
                numDict[keys] += 1

    result = ''
    for keys in numDict.keys():
        result += (keys + ' ') * numDict[keys]
    print(f'#{testcase}')
    print(result)
