arr = [13,3,17,5,15,2,20,12,9]
# 1. 데이터 정렬
arr.sort()

# 2. 반복문을 통해 이진탐색
def bin1(target):
    # 왼쪽 오른쪽 인덱스 구하기
    s = 0
    e = len(arr)-1

    # target을 찾으면 종료 / 더 이상 쪼갤 수 없을 떄까지
    while s <= e:
        mid = (s+e) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target: # target이 범위 왼쪽에 있으면
            e = mid - 1
        else:   # target이 범위 오른쪽에 있으면
            s = mid + 1

    # target을 못 찾으면
    return -1

# 3. 재귀함수를 통해 이진탐색
def bin2(s,e,target):
    # 언제까지 재귀가 반복되어야 할까?
    if s > e:
        return -1
    # 다음 재귀가 들어가기 전에
    # 다음 호출 인자
    mid = (s+e) // 2
    if target == arr[mid] :
        return mid
    
    # 재귀에서 돌아왔을 때 어떤 작업을 해야할까
    if target < arr[mid]:
        return bin2(s,mid-1,target)
    else:
        return bin2(mid+1,e,target)

print(f'20 index num = {bin1(20)}')
print(f'20 index num = {bin2(0,len(arr)-1,20)}')