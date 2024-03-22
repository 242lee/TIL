'''
장후니의 높은 선반
DFS, 백트래킹
단순한 DFS로는 시간 복잡도 너무 커
1
5 16
1 3 3 5 6
-> 1
'''
def dfs(cnt, sumheight):
    global minsum
    # 조건 순서 중요
    # 1. 키의 합이 B 이상이면 종료 -> 탑의 높이 필요
    if sumheight >= B:
        minsum = min(minsum, sumheight)
        return
    # 2. 모든 점원이 탑을 쌓았다면 종료 -> 현재까지 쌓은 점원의 수 필요
    if cnt == N:
        return
    
    # 3. 재귀 호출 - 트리 구조로 호출
    dfs(cnt+1, sumheight + arr[cnt])    # 쌓는다
    dfs(cnt+1, sumheight)               # 안쌓는다

T = int(input())    
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    minsum = 50 ** 20
    dfs(0,0)
    print(f'#{tc} {abs(minsum - B)}')