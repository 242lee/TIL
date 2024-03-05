'''
5
4 1 5 2 3
5
1 3 7 9 5
'''
def binary(target, lst):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            return 1
        elif lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
    return 0

import sys 
input = sys.stdin.readline

N = int(input())
Alist = list(map(int, input().split()))
Alist.sort()

M = int(input())
check = list(map(int, input().split()))

for i in range(M):
    print(binary(check[i], Alist))