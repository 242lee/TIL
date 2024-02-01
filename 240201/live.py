# def binarysearch(arr,N, key):
#     #구간 초기화
#     start = 0
#     end = N-1

#     #검색 구간이 유효하면 반복
#     while start <= end:
#         #중앙에 위치한 값의 인덱스
#         middle = (start+end)//2 #검색 성공
#         if arr[middle] == key:
#             return middle
#         elif arr[middle] > key:
#             end = middle - 1 
#         else:
#             start = middle + 1
#     return -1  #검색 실패


def selectionsort(a,N):
    #구간의 시작을 정의
    for i in range(N-1): #두 개의 원소가 남을 때까지
        #구간의 최소값 위치 minindex, 첫 원소를 최소로 가정
        minindex = i
        #실제 최솟값을 누구니
        for j in range(i+1, N):
            if a[minindex] > a[j]:
                minindex = j
        #찾으면 맨 앞으로 가져다놔
        a[minindex], a[i] = a[i], a[minindex]

N = 5
arr = [1,3,2,5,4]
print(arr)
selectionsort(arr,N)
print(arr)
