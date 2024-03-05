'''
[출력값이 i 인 리스트]  ==> 출력값 i
[2, 3, 4, 5, 6, 7]      ==> 1
[8, 9, ... ,     19]    ==> 2
[20, 21, ...,   37]     ==> 3
...
'''
target = int(input())

limit = 1

for i in range(target):
    limit += i*6  # limit이 7, 19, 37로 계속해서 올라감
    if target <= limit:
        print(i+1)
        break