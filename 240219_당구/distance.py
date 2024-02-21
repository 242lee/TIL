'''
import math

# 두 점의 좌표 (x1, y1), (x2, y2)
x1, y1 = 3, 4  # 예시로 (3, 4)와 (6, 8)을 사용하겠습니다.
x2, y2 = 6, 8

# 밑변과 높이 계산
base = x2 - x1
height = y2 - y1

# 거리 계산
distance = math.sqrt(base**2 + height**2)

print("두 점 사이의 거리:", distance)

'''