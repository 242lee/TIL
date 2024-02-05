T= int(input())
for testcase in range(1, T+1):
    N = input().split()
    numList = list(input().split())
    dict = {}

    for num in numList:
        if dict.get(num):
            dict[num] += 1
        else:
            dict[num] = 1    

    result = ''
    my_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in my_list:
        result += dict.get(i) * (i +' ')
        #i 가 숫자가 아님.. 앞으로는 i를 쓰지 말 것
    print(f'#{testcase}')
    print(result)