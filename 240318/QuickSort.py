# def quick_sort(arr):
#     def sort(low, high):
#         if high <= low:
#             return

#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)

#     def partition(low, high):
#         c = arr[(low + high) // 2]
#         while low <= high:
#             while arr[low] < c:
#                 low += 1
#             while arr[high] > c:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low + 1, high - 1
#         return low

#     return sort(0, len(arr) - 1)
'''
13 3 5 15 2 20 13 9 12
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
arr = list(map(int, input().split()))
result = quick_sort(arr)
print(result)