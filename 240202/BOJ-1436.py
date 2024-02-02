Num = 187

number = 600
asw = 0
while 0 < number:
    cnt = 0
    for n in list(map(int, str(number)[-3:])):
        if n == 6:
            cnt += 1
    if 3 == cnt:
        print(number)
        
    number += 1
    asw += 1
    if asw == Num:
        print(number)
        break


