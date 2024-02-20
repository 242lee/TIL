'''
왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트
완전이진트리에 칸 번호를 붙이고
중위탐색을 해서 번호 넣기
'''
def inorder(T, N):
    global cnt
    if T <= N:
        inorder(T*2, N) # 왼쪽
        tree[T] = cnt
        cnt += 1
        inorder(T*2+1, N) # 오른쪽

T = int(input())
for t in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1) # 비어있는 완전이진트리
    cnt =1
    inorder(1,N)
    print(f'#{t} {tree[1]} {tree[N//2]}')