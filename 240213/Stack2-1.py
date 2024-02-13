def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end = ' ')
        print()
    else:
        for j in range(2):
            bit[i] = j
            f(i+1, k)
N = 4
arr = [1,2,3,4]
bit = [0] * N   # bit[i]: arr[i]가 부분집합에 포함되어 있는지 나타내는 배열
f(0, N)