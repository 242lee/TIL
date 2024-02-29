'''
3
10 7 6
'''
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    price = price[::-1]
    earn = 0
    saleprice = price[0]
    # print(price)
    for i in range(N):
        if saleprice > price[i]:
            earn += saleprice - price[i]
        elif saleprice < price[i]:
            saleprice = price[i]
    print(f'#{tc} {earn}')
#=================================================
# 이건 왜 안 될까유?
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    price.reverse()
    earn = 0
    saleprice = price[0]
    i = 0
    # print(price)
    while True:
        if i == N:
            break
        if saleprice >= price[i]:
            earn += saleprice - price[i]
        elif saleprice < price[i]:
            saleprice = price[i]
        i += 1
    print(f'#{tc} {earn}')  