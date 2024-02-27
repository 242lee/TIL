# # 중복 순열을 for문으로 만들기
# for a in range(1, 4):
#     for b in range(1, 4):
#         for c in range(1, 4):
#             for d in range(1, 4):
#                 print(a,b,c,d)

## ==================================

# def new(depth):
#     if depth == 6:
#         return
#     print(depth, end =' ')
#     new(depth+1)
#     print(depth, end = ' ')
# new(0)

# def new2(depth):
#     if depth == 3:
#         return
#     for i in range(2):
#         new2(depth+1)
# new2(0)

## =====================================
result = []
def per(depth):
    if depth == 3:
        print(result)
        return
    for i in range(1,7):
        result.append(i)
        per(depth+1)
        result.pop()
# per(0)

result2 = []
def per2(depth):
    if depth == 5:
        print(result2)
        return
    for i in range(1, 5):
        result2.append(i)
        per2(depth+1)
        result2.pop()
# per2(0)

## =====================================
N = 3
visited = [0] * 7
result = []
def per(depth):
    if depth == N:
        print(result)
        return
    for i in range(1,7):
        if visited[i] == 0:
            result.append(i)
            visited[i] = 1
            per(depth+1)
            result.pop()
            visited[i] = 0 
# per(0)

## =======================================
            
#1 N개의 주사위를 던져 나올 수 있는 모든 중복순열
N = 2
t1 = []
def type1(depth):
    if depth == N:
        print(t1)
        return
    for i in range(1, 7):
        t1.append(i)
        type1(depth+1)
        t1.pop()
# type1(0)
        
# 2 N개의 주사위를 던져 나올 수 있는 순열
N = 2
t1 = []
visited = [0] * 7
def type2(depth):
    if depth == N:
        print(t1)
        return
    for i in range(1, 7):
        if visited[i] == 0:
            t1.append(i)
            visited[i] = 1
            type2(depth+1)
            t1.pop()
            visited[i] = 0
type2(0)