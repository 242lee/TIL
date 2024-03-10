N = int(input())
stick = 64
cnt = 0
while stick > 0:
    if stick > N:
        stick = stick // 2
    else:
        cnt += 1
        N -= stick
print(cnt)

#     now = stick.pop()
#     shoter = now//2
#     longer = now - shoter
#     stick.append(longer)
#     stick.append(shoter)
#     cnt += 1
#     if now == 1:
#         break
# print(stick)
    