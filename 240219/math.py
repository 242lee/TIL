'''
import math

def distance_between_points(x1, y1, x2, y2):
    # 두 점 사이의 x, y 좌표 차이 계산
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    # 두 점 사이의 각도 계산
    theta = math.atan2(delta_y, delta_x)
    
    # 직각 삼각형을 이용하여 거리 계산
    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
    
    return distance

# 예시
x1, y1 = 0, 0
x2, y2 = 3, 4
print("두 점 사이의 거리:", distance_between_points(x1, y1, x2, y2))
'''