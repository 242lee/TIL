# def countingSort(DATA, TEMP, k):
#     #DATA[] 입력배열(0, k)
#     #TEMP[] 정렬된 배열
#     #Counts[] 카운트 배열

#     Counts = [0] * k #최대수만큼 칸을 만들어

#     for i in range(0, len(DATA)):
#         Counts[DATA[i]] += 1
#         print(Counts)
    
#     for i in range(1, k+1):
#         Counts[i] += Counts[i-1]
#         print(Counts)

#     for i in range(len(TEMP)-1, -1, -1):
#         Counts[DATA[i]] -= 1
#         TEMP[Counts[DATA[i]]] = DATA[i]
#         print(Counts)

# arr = [0,4,1,3,1,2,4,1]
# TempCounts = []
# k = max(arr)

# countingSort(arr, TempCounts, k)
# print(arr)

DATA = [5,4,1,3,1,2,4,1]
k = max(DATA) + 1
Counts = Counts = [0] * k


# Counts 배열에 개수 넣기
for num in DATA:
    Counts[num] +=1
print(Counts) #[0, 3, 1, 1, 2, 1]

# 이것을 누적합으로 바꾸기
for i in range(1, len(Counts)):
    Counts[i] += Counts[i-1]
print(Counts) #[0, 3, 4, 5, 7, 8]

# 이것을 다시 분해하기
result = [0] * len(DATA)
for num in DATA:
    idx = Counts[num]
    result[idx-1] = num
    Counts[num] -= 1
print(result) #[1, 1, 1, 2, 3, 4, 4, 5]