'''
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''
N = int(input())
lst = []
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    lst.append([age, name])
# print(lst)

lst.sort(key = lambda x : x[0])
# print(lst)
for l in range(N):
    print(*lst[l])