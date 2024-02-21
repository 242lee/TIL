# 완전이진트리, 삽입
def insert_in(T):
    # 마지막 노드 추가 (완전이지트리 유지)
    global last
    last += 1
    # 마지막 노드에 데이터(키값) 삽입
    h[last] = T
    # '부모 > 자식' 조건이 만족하도록
    c = last
    p = c//2 # 부모 노드 번호
    while c > 1 and (h[p] < h[c]): # 자식이 루트인 경우 제외, p >= 1
        #부모가 있는데 더 작으면
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2

# 완전이진트리, 삽입
def delete(T):
    # 마지막 노드 추가 (완전이지트리 유지)
    global last
    tmp = h[last] #루트의 키 값 보관
    h[1] = h[last]
    last -= 1
    # 새로 옮긴 부모(root)
    p = 1
    c = p * 2
    # 자식이 있으면
    while c <= last:
        # 오른쪽 자식이 있고 왼쪽 자식과 비교했을 때 더 크면
        if c+1 <= last and h[c] < h[c+1]:
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


N = 10
h = [0] * (10+1)
last= 0

numlist = [2,5,3,6,4]
for i in numlist:
    insert_in(int(i))
    print(h)