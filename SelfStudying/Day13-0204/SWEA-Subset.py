# N, K = map(int, input().split())
 
# Arr = [1,2,3,4,5,6,7,8,9,10,11,12]
# ArrList = []

# for i in range(1<<len(Arr)):
#     innerlist = []
#     for j in range(len(Arr)):
#         if i&(1<<j): 
#             innerlist.append(Arr[j])
#     ArrList.append(innerlist)    

# cnt = 0
# for each in ArrList:
#     if len(each) == N and sum(each) == K:
#         cnt += 1
# # print(f'#{testcase} {cnt}')

Arr = [1,2,3,4]
SubsetList = []

for i in range(1<<(len(Arr))):
    Subset = []
    for j in range(len(Arr)):
        if i&(1<<j):
            Subset.append(Arr[j])
    print(Subset)