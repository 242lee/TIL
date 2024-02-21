def valuesum(p):
    lc = p * 2      # 왼쪽 자식
    rc = p * 2 + 1  # 오른쪽 자식
    # 자식이 있는지 확인
    if lc <= N:
        if rc <= N:
            # 양쪽 다 있으면 합을 반환
            return valuesum(lc) + valuesum(rc)
        else:
            # 왼쪽만 있으면 왼쪽자식 값을 반환
            return valuesum(lc)
    else: # 없으면 자기자신
        return Tree[p]
T = int(input())
for testcase in range(1, T+1):
    N, M, L = map(int, input().split())
    Tree = [0] * (N+1)
    for _ in range(M):
        i, Tree[i] = map(int, input().split())
    print(f'#{testcase} {valuesum(L)}')

