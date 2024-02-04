def BubbleSort(Arr,N):
    for i in range(N):  
        for j in range(N-1):
            if  Arr[j+1] < Arr[j] :
                Arr[j], Arr[j+1] = Arr[j+1], Arr[j]

Arr = [1,5,3,2,4]
BubbleSort(Arr,5)
print(Arr)