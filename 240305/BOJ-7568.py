'''
키 x, 몸무게 y
1. 키로 정렬
2. 몸무게로 정렬

다음 거랑 키, 몸무게 둘 다 비교
둘 다 크면 순위, 아니면 이전과 같은 순위
'''
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

for a in lst:
    rank = 1
    for b in lst:
        if a[0] < b[0] and a[1] < b[1]:
            rank +=1
    print(rank, end = ' ')

'''
a랑 b를 설정해. a가 나, b가 비교대상
키, 몸무게가 나보다 큰 항목이 있으면 rank가 내려가 (+=1)
'''