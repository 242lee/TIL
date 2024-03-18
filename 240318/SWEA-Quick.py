'''
10
7 5 4 1 2 10 3 6 9 8
'''
'''
def mergesort(inputList):
    if len(inputList) == 1:
        return inputList
    mid = len(inputList) // 2
    lList = inputList[:mid]
    rList = inputList[mid:]
    lList = mergesort(lList)
    rList = mergesort(rList)
    return merge(lList, rList)

def merge(lList, rList):
    result = [0]* (len(lList)+len(rList))
    i = j = 0 # i는 lList 배열에서 비교할 위치, j는 rList에서 비교할 위치
    while len(lList) > i and len(rList) > j:
        if lList[i] <rList[j]:
            result[i+j] = lList[i]
            i += 1
        else:
            result[i+j] = rList[j]
            j += 1
        
    while i< len(lList):
        result[i+j] = lList[i]
        i += 1
    while j< len(rList):
        result[i+j] = rList[j]
        j += 1
    return result
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    c = arr[len(arr) // 2]
    smaller, same, bigger = [], [], []
    for num in arr:
        if num < c:
            smaller.append(num)
        elif num > c:
            bigger.append(num)
        else:
            same.append(num)
    return quick_sort(smaller) + same + quick_sort(bigger)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int,input().split()))
    ans= quick_sort(A)
    print(f'#{tc} {ans[N//2]}')