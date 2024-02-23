def allparts(arr):
    result = []
    def parts(arr, fixed):
        if len(arr) == 0:
            return
        for i in range(len(arr)):
            newfixed = fixed + [arr[i]]
            result.append(newfixed[:])
            newarr = arr[i+1:]
            parts(newarr, newfixed)
    parts(arr,[])
    return result

T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = [i+1 for i in range(12)]
    cnt = 0
    for each in allparts(arr):
        if len(each) == N and sum(each) == S:
            cnt += 1
    print(f'#{tc} {cnt}')