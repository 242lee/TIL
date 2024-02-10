def check(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0
T= int(input())
for testcase in range(1, T+1):    
    str1 = input()
    str2 = input()
    print(f'#{testcase} {check(str1, str2)}')