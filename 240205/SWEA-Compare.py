T= int(input())
for testcase in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0
    for i in range(0, len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            ans += 1
        else:
            ans += 0
    print(f'#{testcase} {ans}')