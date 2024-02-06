T = int(input())
for testcase in range(1, T+1):
    Wordlist, saved = list(input().split())
    N = len(Wordlist)
    M = len(saved)
    cnt = N
    for i in range(N-M+1):
        if Wordlist[i:i+M] == saved:
            cnt -= 1 * (M-1)

    print(f'#{testcase} {cnt}')