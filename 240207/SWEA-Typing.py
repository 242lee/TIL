'''
240206 실습 문제
타이핑
banana bana #3
asakusa sa #5
'''
T = int(input())
for testcase in range(1, T+1):
    Wordlist, saved = list(input().split())
    N = len(Wordlist)
    M = len(saved)
    result = N
    i = 0
    while i <= N-M:
        cnt = 0
        for j in range(M):
            if Wordlist[i+j] == saved[j]:
                cnt += 1
        if cnt == M:
            result = result - M + 1
            #같으면 saved 글자 수 만큼 건너 뛰어
            #i += cnt도 되고 M도 되고
            i += M
        else:
            i += 1
    
    print(f'#{testcase} {result}')