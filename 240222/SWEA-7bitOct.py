def calc(each):
    result = 0
    for i in range(len(each)):
        if each[i] == '1':
            result += 2 ** (6-i)
    return result

T = int(input())
for tc in range(1, T+1):
    inputList = list(input())
    resultList = []
    for i in range(10):
        each = inputList[7*i:7*i+7]
        # print(each)
        resultList.append(calc(each))
    print(f'#{tc}', *resultList)

#--------------------------------
'''
T = int(input())
for case in range(1, T+1):
    b = list(map(int, input()))
 
    dec = [0] * 10
    for i in range(10):
        for j in range(7):
            dec[i] += b[i*7 + j] * 2**(6-j)
 
    print(f'#{case}', *dec)
'''