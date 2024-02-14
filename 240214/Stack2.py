def f(i, k):
    if i == k:
        subsetSum = 0
        for j in range(k):
            if bit[j] == 1: # A[j]가 포함된 경우
                subsetSum += A[j]
        if subsetSum == 10:
            for j in range(k):
                if bit[j] == 1:
                    print(A[j], end = ' ')
            print()
            ''' 
            1 2 3 4 
            1 2 7 
            1 3 6
            1 4 5
            1 9
            2 3 5
            2 8
            3 7
            4 6
            10
            '''
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)

N = 10
A =[1,2,3,4,5,6,7,8,9,10]
bit = [0] * N # bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0, N)