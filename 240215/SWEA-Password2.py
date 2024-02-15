from collections import deque
for testcase in range(1, 11):
    N = int(input())
    origin = deque(map(int, input().split()))

    # 비밀번호 마지막 자리가 0이 아닌 동안은 계속 실행
    while origin[-1] != 0:
        for i in range(1,6):
            newnum = origin.popleft() - i
            if newnum <= 0:
                newnum = 0
                origin.append(newnum)
                break
            origin.append(newnum)
    print(f'#{testcase}',*origin)
'''
from collections import deque
 
for _ in range(10):
    tc = int(input())
    password_li = deque(map(int,input().split()))
 
    while password_li[-1] > 0:
        for i in range(5):
            now_num = password_li.popleft() - (i+1)
            if now_num <= 0:
                password_li.append(0)
                break
            password_li.append(now_num)
 
    print(f"#{tc}",*password_li)

'''