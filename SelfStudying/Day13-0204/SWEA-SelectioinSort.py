def SelectionSort(Arr, N): #N은 리스트 길이
    for i in range(N):
        minindex = i
        for j in range(i+1, N):
            if Arr[j] < Arr[minindex] :
                minindex = j
        Arr[minindex], Arr[i] = Arr[i], Arr[minindex]
# def SelectionSort(numList, N):
#     for i in range(N):
#         minindex = i
#         for j in range(i+1, N):
#             if numList[minindex] > numList[j]:
#                 minindex = j
#         numList[i], numList[minindex] = numList[minindex], numList[i]

Arr = [1,8,7,5,0]

SelectionSort(Arr, len(Arr))
print(Arr)
