def f(str1, str2, M, N):
    for i in range(N-(M-1)): #텍스트의 비교 시작위치
        for j in range(M):
            if str2[i+j] != str1[j]: #불일치면 다음 시작위치로 가고
                break
        else: #패턴 매칭에 성공했으면
            return 1
    #모든 위치에서 비교가 끝난 경우에는 - 실패한 거임
    return 0

T = int(input())
for testcase in range(1, T+1):
    str1 = input()
    str2 = input()
    M = len(str1)
    N = len(str2)
    
    ans = f(str1, str2, M, N)