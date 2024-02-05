def check_baby(arr):
    #첫 번째 자리
    for i in range(6):
        for j in range(6):  # 두 번째 자리에 들어갈 요소 경우의 수 넣어보기
            if i == j:
                continue
            #겹치지 않는다면,
            for k in range(6):  # k: 세 번째 자리에 들어갈 요소의 인덱스
                if k == i or k == j :
                    continue
                # i,j,k 가 모두 다름
                for a in range(6): # a: 네 번째 자리
                    if a == i or a==j or a == k :
                        continue
                    for b in range(6):
                        if b == i or b == j or b == k or b == a: # b: 다섯 번째 자리
                            continue
                        for c in range(6): # c: 여섯 번째 자리
                            if c == i or c == j or c == k or c == a or c == b:
                                continue

                            # 순열 중에 baby-gin이 있는지 확인하기

                            result = 0 
                            #triplet
                            if arr[i]+1 == arr[j] and arr[i]+2== arr[k]:
                                result += 1
                            #run
                            elif arr[i] == arr[j] and arr[i] == arr[k]:
                                result += 1

                            if arr[a] + 1 == arr[b] and arr[a] + 2 == arr[c]:
                                result += 1
                            elif arr[a] == arr[b] and arr[a] == arr[c]:
                                result += 1

                            if result == 2: # Baby Gin
                                return True
    return False

T = int(input())
for testcase in range(1, T+1):
    arr = list(map(int, input()))
    result = check_baby(arr)
    if result:
        print(f'{testcase} Baby Gin')
    else:
        print(f'{testcase} Lose')
