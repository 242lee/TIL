for _ in range(10):
    tc = int(input())
    origin = list(map(int, input().split()))

    while origin[-1] != 0:
        for n in range(1, 6):
            newnum = origin.pop(0) - n
            if newnum <= 0:
                newnum = 0
                origin.append(newnum)
                break
            origin.append(newnum)
    print(f'#{tc}', *origin)