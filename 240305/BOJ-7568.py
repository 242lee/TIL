'''
키 x, 몸무게 y
1. 키로 정렬
2. 몸무게로 정렬

다음 거랑 키, 몸무게 둘 다 비교
둘 다 크면 순위, 아니면 이전과 같은 순위
'''
N = int(input())
lst = []
rank = [0] * N
for _ in range(N):
    lst.append(list(map(int, input().split())))
print(lst)

# lst.sort(key = lambda x : (x[0], x[1]), reverse= True)
# print(lst)


