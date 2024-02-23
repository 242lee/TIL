'''
11
5 8 3 1 5 6 9 9 2 2 4
'''
for tc in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))

    while N > 0:
        maxh = 0
        minh = 101
        maxindex = 0
        minindex = 0
        for i in range(len(height)):
            if maxh < height[i]:
                maxh = height[i]
                maxindex = i
            if minh > height[i]:
                minh = height[i]
                minindex = i
        # print(maxindex, minindex)

        height[maxindex] -= 1
        height[minindex] += 1
        # print(height)

        N -= 1

    result = max(height) - min(height) 
    print(f'#{tc} {result}')