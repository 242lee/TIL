arr = [1, 2, 1, 3, 2, 4, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

class TreeNode:
    def __init__(self,  value):
        self.value= value
        self.left = None
        self.right = None

    def insert(self, child):
        if not self.left:
            self.left = child
            return
        if not self.right:
            self.right = child
            return
        return
    
    def inorder(self):
        if self!= None:
            # 프린트가 여기있으면 전위
            if self.left:
                self.left.inorder()
            # 여기 있으면 중위
            if self.right:
                self.right.inorder()
            print(self.value, end = '')

# 이진트리 만들기
# 1. 노드 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
# 2. 간선 연결
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].isert(nodes[childNode])