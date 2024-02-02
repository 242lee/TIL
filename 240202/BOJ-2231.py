N = int(input())

flag = False
for num in range(1,N+1):
    sumnum = num
    
    for i in str(num):
        sumnum += int(i)  
    
    if sumnum == N:
        print(num)
        flag = True
        break
    
if flag == False:
    print(0)
#--------------------------------------
        
# sum = 0
# for i in str(N):
#     sum += int(i)
# print(sum)