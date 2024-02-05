def BubbleSort(arr, N):
    for i in range(N-1, 0, -1):
        print(i)
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [1,5,7,2,3,6,4,8]
N = 8

BubbleSort(arr, N)
print(arr)