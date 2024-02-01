T = int(input())
for testcase in range(1, T+1):
    totalPage, Apage, Bpage = map(int, input().split())

    def counting(totalpage, findingpage):
        start = 1
        end = totalpage
        cnt = 0
        while start <= end:
            middle = int((start+end)/2)
            if middle == findingpage:
                cnt += 1
                break
            elif middle > findingpage:
                end = middle - 1
                cnt += 1
            else:
                start = middle + 1
                cnt += 1
        return cnt

    if counting(totalPage, Apage) < counting(totalPage, Bpage):
        print(f'#{testcase} A')
    elif counting(totalPage, Apage) > counting(totalPage, Bpage):
        print(f'#{testcase} B')
    else:
        print(f'#{testcase} 0')
#-------------------------------------------------

# book = range(0, 400)
# start = 1
# end = 400
# cnt = 0
# while start <= end:
#     middle = int((start+end)/2)
#     if book[middle] == 350:
#         cnt += 1
#         break
#     elif book[middle] > 350:
#         end = middle - 1
#         cnt += 1
#     else:
#         start = middle + 1
#         cnt += 1
# print(cnt)