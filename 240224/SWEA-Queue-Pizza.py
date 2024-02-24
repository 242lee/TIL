T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) 
    pizza = [0] + list(map(int, input().split()))
    pizzaindex = [i+1 for i in range(M)]

    oven = list(pizzaindex[:N])
    coldpizza = list(pizzaindex[N:])

    while len(oven) > 1:
        now = oven.pop(0)
        pizza[now] //= 2 
        if pizza[now] != 0 : 
            oven.append(now)
        else :
            if coldpizza :
                oven.append(coldpizza.pop(0))

    last = oven.pop(0)
    print(f'#{tc} {last}')