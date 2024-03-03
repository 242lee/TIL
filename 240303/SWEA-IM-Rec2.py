'''
700 50 800 600
10 10 700 700
직사각형1, 선2, 점3, 공통부부없음4
'''
# T = int(input())
result = []
for _ in range(4):
# [0][1] 왼쪽 아래, [2][3] 오른쪽 위
    inputList = list(map(int, input().split()))
    rec1 = inputList[:4]
    rec2 = inputList[4:]
    # 2. 선이 겹치는 경우
    if rec1[0] == rec2[2] or rec1[2] == rec2[0] or rec1[1] == rec2[3] or rec1[3] == rec2[1]:
        # 3. 점이 만나는 경우
        if (rec1[0] == rec2[2] and rec1[1] == rec2[3]) or (rec1[2] == rec2[1] and rec1[3] == rec2[1]) or (rec1[0] == rec2[2] and rec1[3] == rec2[1]) or (rec1[2] == rec2[0] and rec1[1] == rec2[3]):
            result.append('c')
        else:
            result.append('b')
    # 4. 안 만나는 경우
    elif rec1[0] > rec2[2] or rec1[2] < rec2[0] or rec1[1] > rec2[3] or rec1[3] < rec2[1]:
        result.append('d')
    else: result.append('a')

for i in range(4):
    print(result[i])