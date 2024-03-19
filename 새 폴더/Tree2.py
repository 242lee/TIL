arr = [1, 2, 1, 3, 2, 4, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

nodes = [[] for _ in range(14)] 
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].append(childNode)
# 자식이 없는 걸 표시하기
for li in nodes:
    for _ in range(len(li),1):
        li.append(None)
# 중위
def inorder(nodeNum):
    if nodeNum == None:
        return
    inorder(nodes[nodeNum][0])  # 왼쪽
    print(nodeNum, end = '')
    inorder(nodes[nodeNum][1])  # 오른쪽
    
    