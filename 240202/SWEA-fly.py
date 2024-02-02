# 파리 배열
N = 4
arr = [[1] * N for _ in range(N)]


#----------------------------------

n, m = map(int, input().split())        # 배열을 만들 n 과 파리채를 만들 m을 받는다
arr = [list(map(int, input().split())) for _ in range(n)]


max_df = 0      # 가장 많은 파리가 죽은 수를 저장할 변수 설정 / 0으로 초기화 해준다.

for i in range(n-m+1) :
    for j in range(n-m+1) :
        dead_f = 0      # 죽은 파리의 개수를 셀 변수 설정

        for k in range(m) :     # 파리채 크기만큼 파리를 잡아봅시다!
            for l in range(m) :
                dead_f += arr[i+k][j+l]

        if max_df <= dead_f :   # 잡은 파리와 제일 많이 잡은 파리의 수를 비교해서 더 크면 새로 저장해줌!
            max_df = dead_f

print(f'# {max_df}')