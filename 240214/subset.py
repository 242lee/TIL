def f(i,N,subsetlen,Target):
    global cnt
    subsetsum =0
    if i == N:
        count = 0
        for j in range(N):
            if bit[j] == 1:
                subsetsum += arr[j]
                count += 1
        if subsetsum == Target and count == subsetlen:
            cnt+= 1
    
    else:
        bit[i] = 1
        f(i+1, 12, subsetlen, Target)
        bit[i] = 0
        f(i+1, 12, subsetlen, Target)
    
arr = [1,2,3,4,5,6,7,8,9,10,11,12]

T = int(input())
for testcase in range(1, T+1):
    subsetlen, Target = map(int, input().split())
    N = 12
    cnt = 0
    bit = [0] * N
    f(0,12,subsetlen,Target)
    print(cnt)