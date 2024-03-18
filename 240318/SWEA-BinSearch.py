def binsearch(s,e,target):
    dir = 0
    while s <= e:
        mid = (s+e) // 2
        # 1. mid 가 바로 타겟인 경우
        if target == Alist[mid]:
            return 1
        # 2. 번갈아 탐색하는지 확인하기
        elif target < Alist[mid]: # dir = -1일 때
            if dir == -1:
                return 0
            else:
                e = mid - 1
                dir = -1
        elif target > Alist[mid]: # dir = 1 일 때
            if dir == 1:
                return 0
            else:
                s = mid + 1
                dir = 1
    return 0

T = int(input())
for tc in range(1, T+1):    
    A, B = map(int, input().split())
    Alist = list(map(int, input().split()))
    Blist = list(map(int, input().split()))
    Alist.sort()
    Blist.sort()
    cnt = 0

    for b in Blist:
        cnt += binsearch(0,A-1,b)

    print(f'#{tc} {cnt}')