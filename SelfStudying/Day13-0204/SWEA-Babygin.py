def BabyGin(num, cntList):
    cntList[num] +=1
    flag = False
    i = 0
    while i < 8 :
        if cntList[i] >= 3: # triplet
            flag = True
            break
        if cntList[i] and cntList[i+1] and cntList[i+2]:
            flag = True
            break
        i += 1
    if flag == True:
        return f'Babygin'
    
T = int(input())

for testcase in range(1, T+1):
    cardList = list(map(int, input().split()))
    cnt1, cnt2 = [0] * 10, [0] * 10

    winner = 0
    for i in range(0, len(cardList), 2):
        if BabyGin(cardList[i], cnt1):
            winner = 1
            break
        if BabyGin(cardList[i+1], cnt2):
            winner = 2
            break

print(f'#{testcase} {winner}')
