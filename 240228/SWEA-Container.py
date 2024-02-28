T = int(input())
for tc in range(1, T+1):
    # N개의 컨테이너를 M대의 트럭으로 옮겨
    N, M = map(int, input().split())
    # 화물의 무게
    weight = list(map(int, input().split()))
    weight.sort(reverse=True)
    # 트럭의 적재용량
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)

    # 한 번 만으로 옮길 수 있는 화물의 최대 무게
    move = 0
    t = 0
    w = 0
    while t < M and w < N:
        if weight[w] <= truck[t]:
            move += weight[w]
            w += 1
            t += 1

        else:
            w += 1
    print(f'#{tc} {move}')

# total = 0
# while weight and truck:
#     if weight[0] <= truck[0]:
#         total += weight.pop(0)
#         truck.pop(0)
#     else:
#         weight.pop(0)
# print(total)
