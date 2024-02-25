<<<<<<< HEAD
from collections import deque
for _ in range(10):
    tc = int(input())
    origin = deque(map(int, input().split()))
 
    while origin[-1] != 0:
        for n in range(1, 6):
            newnum = origin.popleft() - n
            if newnum <= 0:
                newnum = 0
                origin.append(newnum)
                break
            origin.append(newnum)
=======
from collections import deque
for _ in range(10):
    tc = int(input())
    origin = deque(map(int, input().split()))
 
    while origin[-1] != 0:
        for n in range(1, 6):
            newnum = origin.popleft() - n
            if newnum <= 0:
                newnum = 0
                origin.append(newnum)
                break
            origin.append(newnum)
>>>>>>> 6cae89679cc613ec6d76d60eb7eb98ceb0ff10a7
    print(f'#{tc}', *origin)