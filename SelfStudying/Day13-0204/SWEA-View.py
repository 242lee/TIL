T = 10
for testcase in (1, T+1):
    N = int(input()) #건물의 수
    buildings = list(map(int, input().split()))
    viewgood = 0

    for height in range(2, N-2):
        maxHeight = 0
        for i in [-2,-1,1,2]: #좌우로 2칸까지 확인
            if maxHeight < buildings[height+i]:
                maxHeight = buildings[height+i]
        if maxHeight < buildings[height]:
            viewgood += buildings[height] - maxHeight
    print(f'#{testcase} {viewgood}')

 
T = 10
for tc in range(1, T+1):
    N = int(input()) #건물의 수
    buildings = list(map(int, input().split())) #N개 건물의 높이
    nice_view = 0 #조망권 확보된 세대 수
    for height in range(2, N-2): #맨 왼쪽 두칸과 맨 오른쪽 두칸을 제외하고 건물 index를 순회
        near_max_h = 0 #인근 건물 중 가장 높은 건물 높이
        # 각 건물의 좌우 2칸내의 건물중 가장 높은 건물의 높이 찾기
        for i in [-2, -1, 1, 2]:
            if near_max_h < buildings[height+i]:
                near_max_h = buildings[height+i]
        # 현 위치의 건물에서 조망권 확보된 세대 수를 찾아서 더해줌
        if buildings[height] > near_max_h:
            nice_view += buildings[height] - near_max_h
    #조망권이 확보된 세대 수 출력
    print(f'#{tc} {nice_view}')
