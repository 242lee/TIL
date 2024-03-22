'''
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300
0 0 0 0 0 0 0 0 6 2 7 8
-> 110
'''
def dfs(month, pricesum):
    global ans
    # 1. 12월까지 다 봤으면 종료
    if month > 12:
        ans = min(ans, pricesum)
        return
    # 2. 이미 최소값을 넘어갔으면 종료
    if pricesum > ans:
        return
    # 모두 일일권으로 구매
    dfs(month + 1, pricesum + (days[month] * price[0]))
    # 모두 한달권 구매
    dfs(month + 1, pricesum + price[1])
    # 모두 tp달권 구매
    dfs(month + 3, pricesum + price[2])
    # 모두 한달권 구매
    dfs(month + 12, pricesum + price[3])
    
T = int(input())
for tc in range(1, T+1):
    price =  list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))
    ans = int(1e9)
    dfs(1, 0)
    print(f'#{tc} {ans}')