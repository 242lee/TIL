from collections import deque

N = int(input())
numList = deque([i+1 for i in range(N)])
while len(numList) > 1:
    numList.popleft()
    numList.append(numList.popleft())
print(*numList)
