T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    meeting = []
    for i in range(N):
        si, ei = arr[i][0], arr[i][1]
        meeting.append((si,ei))
    meeting.sort(key= lambda x: x[1])
    # print(meeting)

    end = 0
    cnt = 0
    for t in range(N):
        if meeting[t][0] >= end:
            cnt += 1
            end = meeting[t][1]
            # print(meeting[t])
    print(f'#{tc} {cnt}')