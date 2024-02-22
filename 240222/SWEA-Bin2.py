digit = []
for i in range(13):
    digit.append(1*(2**(-1*i)))
# print(digit)
T = int(input())
for tc in range(1, T+1):
    Target = float(input())
    check = []
    for i in range(13):
        if digit[i] <= Target:
            Target -= digit[i]
            check.append(i)

        
    # print(check)
        
    result = [0] * check[-1]
    if Target == 0:
        for j in check:
            result[j-1] = 1
        print(f'#{tc}',''.join(map(str, result)))
    else:
        print(f'#{tc} overflow')