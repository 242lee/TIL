hex = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}
T = int(input())
for tc in range(1, T+1):
    N, inputList = input().split()
    resultList = [] * int(N)
    for i in range(len(inputList)):
        resultList.append(hex.get(inputList[i]))
    print(f'#{tc}', ''.join(resultList))
#---------------------------------------
T = int(input())
for tc in range(1, T+1):
    N, inputList = input().split()
    N = int(N)

    resultList = [] * (N + 5)
    for i in range(N):
        resultList.append(hex.get(inputList[i]))
    
    print(f'#{tc}', end= ' ')
    for j in resultList:
        print(j, end = '')
    print()