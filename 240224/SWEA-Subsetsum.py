N, K = map(int, input().split())
arr = [i+1 for i in range(12)]

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
    parts(arr, [])
    return result

# print(allparts(arr))
for each in allparts(arr):
    if sum(each) == K:
        print(each, end = ' ')