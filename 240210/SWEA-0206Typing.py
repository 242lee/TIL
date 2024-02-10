def typing(str1, str2):
    N = len(str1)
    M = len(str2)
    result = N
    i = 0

    while i <= N-M:
        cnt = 0
        for k in range(M):
            if str1[i+k] == str2[k]:
                cnt += 1
        if cnt == M:
            result = result - M +1
            # str1 안에 str2를 발견하면 그만큼 건너뛰어서 다시 시작
            i += M
        else:
            i += 1
    return result

T = int(input())
for testcase in range(1, T+1):
    str1, str2 = list(input().split())
  
    print(f'#{testcase} {typing(str1, str2)}')