T = int(input())

for testcase in range(1, T+1):
    N = int(int(input())//10)
    paper = [0] * (N+1)
    paper[1] = 1
    paper[2] = 3
    for i in range(3, N+1):
        paper[i] = paper[i-1] + (2 * paper[i-2])
    print(f'#{testcase} {paper[N]}')
